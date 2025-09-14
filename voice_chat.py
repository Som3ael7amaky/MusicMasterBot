import os
import asyncio
from pyrogram import Client
from config import Config

class VoiceChatManager:
    def __init__(self):
        self.client = None
        self.initialized = False
        
    async def init_voice_client(self):
        if Config.SESSION_STRING and Config.API_ID and Config.API_HASH:
            try:
                self.client = Client(
                    "music_bot",
                    api_id=Config.API_ID,
                    api_hash=Config.API_HASH,
                    session_string=Config.SESSION_STRING
                )
                await self.client.start()
                self.initialized = True
                print("Voice chat client initialized successfully")
            except Exception as e:
                print(f"Failed to initialize voice client: {e}")

    async def join_voice_chat(self, chat_id):
        if not self.initialized:
            return False, "Voice client not initialized"
        
        try:
            await self.client.join_chat(chat_id)
            return True, "Joined voice chat successfully"
        except Exception as e:
            return False, f"Failed to join voice chat: {e}"

voice_manager = VoiceChatManager()