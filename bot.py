import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")

client = discord.Client()

@client.event 
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return
    if message.content == "huh": 
        await message.channel.send("HUH")

@client.event
async def on_message(message:discord.Message):
    if message.author.bot:
        return
    if message.content == "Hi":
        await message.channel.send("Hi bubba")


client.run(TOKEN)