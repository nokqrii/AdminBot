import os
import discord
from discord.ext import commands
import requests

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix="n!", intents=intents)

def get_dad_joke():
    url = "https://icanhazdadjoke.com/"
    headers = {"Accept": "application/json"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        joke_data = response.json()
        return joke_data['joke']
    except requests.exceptions.RequestException as e:
        return f"Could not fetch joke: {e}"

@bot.event
async def on_ready():
    print(f"Great! The bot {bot.user} is online.")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello! I am a Python bot built from scratch!")
@bot.command()
async def ping(ctx):
    await ctx.send("Pong")
@bot.command()
async def server(ctx):
    embed = discord.Embed(
        title=ctx.guild.name,
        description=(
            f"Members: {len(ctx.guild.members)}\n"
            f"Owner: {ctx.guild.owner}\n"
            f"Channels: {len(ctx.guild.channels)}\n"
            f"Roles: {len(ctx.guild.roles) - 1}\n"
            f"Server ID: {ctx.guild.id}\n"
            f"Created at: {ctx.guild.created_at}\n"
            f"Description: {ctx.guild.description}"
        )
    )
    if ctx.guild.icon:
        embed.set_thumbnail(url=ctx.guild.icon.url)
    await ctx.send(embed=embed)
@bot.command()
async def joke(ctx):
    await ctx.send(get_dad_joke())
@bot.command()
async def user(ctx):
    await ctx.send(f"Username: {ctx.author}")

bot.run(os.getenv("token"))