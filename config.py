import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Bot Token from @BotFather
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    
    # API ID and Hash from my.telegram.org
    API_ID = int(os.getenv("API_ID", 123456))
    API_HASH = os.getenv("API_HASH", "your_api_hash_here")
    
    # Bot Owner ID
    OWNER_ID = int(os.getenv("OWNER_ID", 123456789))
    
    # Database URL
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///database.db")
    
    # Music Settings
    MAX_PLAYLIST_SIZE = 100
    SONG_DOWNLOAD_DIR = "/tmp/music_bot"
    
    # Voice Chat Settings
    SESSION_STRING = os.getenv("SESSION_STRING", "")
    
    # API Keys
    CAT_API_KEY = os.getenv("CAT_API_KEY", "")
    DOG_API_KEY = os.getenv("DOG_API_KEY", "")
    
    # Developer IDs
    DEVELOPERS = [OWNER_ID]
    
    # Log Channel
    LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", -1001234567890))