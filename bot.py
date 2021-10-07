from discord import member, message
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
    print("Bot is ready.")


@client.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return
    if "huh" in message.content:
        await message.channel.send("HUH")
    if message.content == "Nigga":
        await member.ban(reason="Racist")
    if message.content == "luminor help":
        embedVar = discord.Embed(
            title="Hi! I'm Luminor", description="", color=0x6C5CE7
        )
        embedVar.add_field(
            name="Welcome to the help centre!", value="huh", inline=False
        )
        await message.channel.send(embed=embedVar)
    if "luminor meme" in message.content:
        memes_submissions = reddit.subreddit("memes").hot()
        post_to_pick = random.randint(1, 10)
        for i in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)
            ups = submission.score
            comments = submission.num_comments
            link = submission.permalink
        embedVar = discord.Embed(
            title=submission.title,
            url=f"https://reddit.com{link}",
            description="",
            color=0x6C5CE7,
        )
        embedVar.set_image(url=submission.url)
        embedVar.set_footer(text=f"👍 {ups} 💬 {comments}")
        await message.channel.send(embed=embedVar)

    if "luminor slots" in message.content:
        responses = ["🍋", "🍊", "🍉", ":seven:"]
        respInEmbed = (
            random.choice(responses)
            + random.choice(responses)
            + random.choice(responses)
        )
        embedSlots = discord.Embed(
            title="🎰 Slot Machine 🎰", description=respInEmbed, color=0x176CD5
        )
        embedSlots.set_footer(text="You need triple 7's to win.")
        await message.channel.send(embed=embedSlots)
        if respInEmbed == ":seven::seven::seven:":
            embedWin = discord.Embed(
                title="🎉 You Won!",
                description="You got three :seven:'s! GGs",
                color=message.author.color,
            )
            await message.channel.send(embedWin=embedWin)


keep_alive()
client.run(TOKEN)
