import discord
from discord.ext import commands
import logging # https://discordpy.readthedocs.io/en/stable/logging.html
import json
import message_handler

def getInfo(path):
    file = open(path)
    json_data = json.load(file)

    return json_data


token = getInfo("simpel_bot/info.json")["token"]
    
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"{client.user}, Status: {client.status}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if str(message.channel) != "bot_commands":
        return

    if not message.content.startswith("!"):
        return
    

    await message.channel.send("Hello")

client.run(token)
