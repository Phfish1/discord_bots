import discord
from discord.ext import commands

import youtube_handler

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

music_que = []

@bot.command()
async def play(context, *args):
    print("PLAYING SONG")
    arguments = " ".join(args)

    song_info = await youtube_handler.search_youtube(arguments)
    formated_song_info = f"{song_info['title']}, av {song_info['channel']['name']} ({song_info['duration']})\n{song_info['link']}"

    youtube_download_title = await youtube_handler.download_song(song_info["link"])

    author_channel = context.author.voice.channel

    if context.voice_client == None: 
        await author_channel.connect()
    
    ### PLAY SONG HERE
    ffmpeg_options = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    context.voice_client.play(discord.FFmpegAudio(executable="command_bot/ffmpeg/ffmpeg", source=f"songs/{youtube_download_title}.mp4", args=""))



    await context.send(f"Playing song: {formated_song_info}")

@bot.command()
async def die(context):
    await context.voice_client.disconnect()

bot.run("MTE1MjcyMjIwMzgyNjIxMjkyNA.GKbd9E.WkNcA65NJsfj-YYoKK0Rdr3mjlz-eLn90t0RTY")
