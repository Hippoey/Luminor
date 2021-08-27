from discord import message
import praw
import random
from keep_alive import keep_alive
import discord
from discord.ext import commands
from discord.ext import tasks
import os
from dotenv import load_dotenv
import random

load_dotenv()

TOKEN = os.getenv("TOKEN")

client = discord.Client()

reddit = praw.Reddit(client_id='Dec7VPO9YEnNZ2vK_Bhu1w',
                     client_secret='Ol-trTNDxYAM3MM8LPQz5Qx0FmHK2w',
                     user_agent='imyourmother')

@tasks.loop(minutes=20)
async def test():
    channel = client.get_channel(868076426312704021)
    message = ["What's that?", "You got that drip? Dayum bro!", "Hello there", "@665488298533322762" ]
    await channel.send(message[random. randint(0,3)])

@client.event 
async def on_ready():
   activity = discord.Game(name=("luminor help"), type=3)
   test.start()
   await client.change_presence(status=discord.Status.idle, activity=activity)
   print('Bot is ready .')

@client.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return
    if "huh" in message.content: 
        await message.channel.send("HUH")
    if message.content =='luminor help':
        embedVar = discord.Embed(title="Hi! I'm Luminor", description="", color=0x6c5ce7)
        embedVar.add_field(name="Welcome to the help centre!", value="huh", inline=False)
        await message.channel.send(embed=embedVar)
    if "nigger" in message.content:
        await message.author.ban(reason="Racist", delete_message_days=7)
    if "nigga" in message.content:
        await message.author.ban(reason="Racist", delete_message_days=7)
    if "Nigga" in message.content:
        await message.author.ban(reason="Racist", delete_message_days=7)
    if "Nigger" in message.content:
        await message.author.ban(reason="Racist", delete_message_days=7)
    if "NIGGER" in message.content:
        await message.author.ban(reason="Racist", delete_message_days=7)
    if "NIGGA" in message.content:
        await message.author.ban(reason="Racist", delete_message_days=7)
    if "luminor meme" in message.content:
        memes_submissions = reddit.subreddit('memes').hot()
        post_to_pick = random.randint(1, 10)
        for i in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)

        embedVar = discord.Embed(title="Meme", description="", color=0x6c5ce7)
        embedVar.set_image(url=submission.url)
        await message.channel.send(embed=embedVar)




keep_alive() 
client.run(TOKEN)