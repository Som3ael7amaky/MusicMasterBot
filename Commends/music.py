from telegram import Update
from telegram.ext import CallbackContext
from music_core import MusicCore

music_core = MusicCore()

async def play_command(update: Update, context: CallbackContext):
    if not context.args:
        await update.message.reply_text("🚦 اكتب اسم الأغنية بعد الأمر! مثال: /play أغنية")
        return
    
    query = " ".join(context.args)
    await update.message.reply_text(f"🔍 جاري البحث عن: {query}")
    
    results = await music_core.search_song(query)
    if not results:
        await update.message.reply_text("❌ ما لقيتش الأغنية دي!")
        return
    
    song = results[0]
    await update.message.reply_text(f"📥 جاري التحميل: {song['title']}")
    
    # هنا سيتم تحميل وتشغيل الأغنية
    await update.message.reply_text(f"🎵 الآن يتم تشغيل: {song['title']}")

async def skip_command(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    if await music_core.skip_song(chat_id):
        await update.message.reply_text("⏭️ تم تخطي الأغنية!")
    else:
        await update.message.reply_text("❌ مافيش أغاني في قائمة الانتظار!")