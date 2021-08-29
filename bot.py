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

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CRED_ID"),
    client_secret=os.getenv("REDDIT_CRED_SECRET"),
    user_agent="imyourmother",
)


@tasks.loop(minutes=20)
async def test():
    channel = client.get_channel(881035045765275720)
    message = [
        "What's that?",
        "You got that drip? Dayum bro!",
        "Hello there",
        "HUH",
        "Sheeeeeeeesh!!!!!!",
        "Baba Boeey",
        "That's cap!",
        "baaaap",
        "What's the time?",
        "How could this happen to me",
        "https://tenor.com/view/dead-chat-gif-22605399",
    ]
    await channel.send(message[random.randint(0, 10)])


@client.event
async def on_ready():
    activity = discord.Game(name=("luminor help"), type=3)
    test.start()
    await client.change_presence(status=discord.Status.online, activity=activity)
    print("Bot is ready .")


@client.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return
    if "huh" in message.content:
        await message.channel.send("HUH")
    if message.content == "luminor help":
        embedVar = discord.Embed(
            title="Hi! I'm Luminor", description="", color=0x6C5CE7
        )
        embedVar.add_field(
            name="Welcome to the help centre!", value="huh", inline=False
        )
        await message.channel.send(embed=embedVar)
    if "luminor censor this word" in message.content:
        await message.channel.send("What word would that be?")

        def check(m: discord.Message):
            return m.author.id == message.author.id and m.channel == message.channel

        msg = await client.wait_for("message", check=check)
        await message.channel.send(f"Word censored!")
    if "luminor meme" in message.content:
        memes_submissions = reddit.subreddit("memes").hot()
        post_to_pick = random.randint(1, 10)
        for i in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)

        embedVar = discord.Embed(title="Meme", description="", color=0x6C5CE7)
        embedVar.set_image(url=submission.url)
        await message.channel.send(embed=embedVar)


keep_alive()
client.run(TOKEN)
