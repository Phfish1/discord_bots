from youtubesearchpython import VideosSearch
import pytube

async def search_youtube(song_search):
    search_query = VideosSearch(song_search, limit=1)
    search_result = search_query.result()["result"][0]

    return search_result
    


    #for result in search_result:
    #    song = result["title"]
    #    artist = result["channel"]["name"]
    #    song_duration = result["duration"]
    #    url = result["link"]

async def download_song(link):
    yt = pytube.YouTube(link)
    yt.streams.get_audio_only().download(output_path="command_bot/songs")

    return str(yt.title)


