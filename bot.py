import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time



adminID = ""
Client = discord.Client()
bot = commands.Bot(command_prefix="$")


@bot.event
async def on_ready():
    print("Bot is ready!")

@bot.event
async def on_message(message):
    if message.author != bot:
        await bot.send_message(message.channel, "FUCKING HACK ME NOW YOU TWAT")

while True:
    bot.run('NTIyMDc0NjA3MTU5NzM4Mzcx.DvFrag.EOoLoiR6_dKQFlt0gEba1C3xgmY')
