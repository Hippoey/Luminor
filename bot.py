import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '*')

@client.event 
async def on_ready():
    print('Bot is ready.')

client.run('ODY5ODc0OTE5OTU2MTg1MTQ4.YQEkJg.cidK38_4e7bFr00znvuFKVulj8U')
