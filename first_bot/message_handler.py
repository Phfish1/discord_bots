import discord

import bot

async def normal_message(message):
    user_message = message.content.lower()

    if user_message == "hei":
        await message.channel.send("Hello")

    