from keep_alive import keep_alive
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")

client = discord.Client()

@client.event 
async def on_ready():
    print('Bot is ready .')

@client.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return
    if "huh" in message.content: 
        await message.channel.send("HUH")
    if message.content == "hi":
        await message.channel.send("Hello")
    if message.content == "sheesh":
        await message.channel.send("<@665488298533322762>", delete_after=0.5)
        await message.delete()
    if message.content =='luminor':
        embedVar = discord.Embed(title="Hi! I'm Luminor Bot", description="", color=0x6c5ce7)
        await message.channel.send(embed=embedVar)

keep_alive() 
client.run(TOKEN)