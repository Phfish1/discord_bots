import discord
from discord.ext import commands

import youtube_handler

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

music_que = []

@bot.command()
async def play(context, *args):
    arguments = " ".join(args)

    if "https://" in arguments:
        youtube_download = await youtube_handler.download_song(arguments)
        formated_song_info = f"{youtube_download.title}, av {youtube_download.author} ({youtube_download.length})"
    else:
        song_info = await youtube_handler.search_youtube(arguments)
        formated_song_info = f"{song_info['title']}, av {song_info['channel']['name']} ({song_info['duration']})\n{song_info['link']}"

        youtube_download = await youtube_handler.download_song(song_info["link"])

    author_channel = context.author.voice.channel

    if context.voice_client == None:
        print(f"joining channel: {author_channel}")
        await author_channel.connect()
    
    print("PLAYING SONG")
    ### PLAY SONG HERE
    #ffmpeg_options = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    context.voice_client.play(discord.FFmpegAudio(source=f"command_bot/songs/{str(youtube_download.title)}.mp4", args=""))
    #context.voice_client.play("hei")


    await context.send(f"Playing song: {formated_song_info}")

@bot.command()
async def die(context):
    await context.voice_client.disconnect()

bot.run("MTE1MjcyMjIwMzgyNjIxMjkyNA.Gq9hqW.zOlxNMcJ2BGvxFE_wtthHPEJAWL0mTOcTCw3vo")
