import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix="n!", intents=intents)

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
    await ctx.send(
        f"Server's name is: {ctx.guild.name}\n"
        f"Members: {len(ctx.guild.members)}\n"
        f"Owner: {ctx.guild.owner}\n"
    )

bot.run(os.getenv("token"))