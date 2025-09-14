import os
import yt_dlp
import asyncio
from youtube_search import YoutubeSearch
from config import Config

queues = {}
current_playing = {}

class MusicCore:
    def __init__(self):
        self.ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': os.path.join(Config.SONG_DOWNLOAD_DIR, '%(title)s.%(ext)s'),
            'quiet': True,
        }

    async def search_song(self, query, max_results=5):
        try:
            results = YoutubeSearch(query, max_results=max_results).to_dict()
            return results
        except Exception as e:
            print(f"Search error: {e}")
            return []

    async def download_song(self, url):
        try:
            with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                filename = ydl.prepare_filename(info)
                if filename.endswith('.webm'):
                    filename = filename[:-5] + '.mp3'
                return filename, info.get('title', 'Unknown'), info.get('duration', 0)
        except Exception as e:
            print(f"Download error: {e}")
            return None, None, 0

    async def add_to_queue(self, chat_id, song_info):
        if chat_id not in queues:
            queues[chat_id] = []
        queues[chat_id].append(song_info)
        return len(queues[chat_id])