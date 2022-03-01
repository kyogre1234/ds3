
import os
import difflib
import sqlite3
import discord
from discord.ext import commands
from discord.ext import tasks
import asyncio
from keep_alive import keep_alive
import requests
from discord_webhook import DiscordWebhook


cid = 914006283038904370
TOKEN = os.getenv("TOKEN")



editing = {

}
req = requests.get("https://discord.com/api/path/to/the/endpoint")

print(req)
import time
import random

client = commands.Bot(command_prefix='$@#')

client._skip_check = lambda x, y: False

@tasks.loop(seconds=0.2)
async def spammer():
  text_channel = client.get_channel(cid)

  if text_channel != None:
    words = "-roll 100"
    #num = random.randint(1,10000000000000000000000000)
    await text_channel.send(words)
    intervals = [2]
    await asyncio.sleep(random.choice(intervals))

@tasks.loop(seconds=14400)
async def sleeper():
  time.sleep(seconds = 3600)
  spammer.start()
spammer.start()

@client.command()
async def stop(ctx):
    spammer.stop()

@client.command()
async def spam(ctx):
  spammer.start()

keep_alive()
client.run(TOKEN,bot=False)
