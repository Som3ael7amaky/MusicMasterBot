import logging
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from config import Config
from helpers.database import init_db
from commands import basic, music, games, fun, admin, dev
from commands.admin import mute_command, ban_command, admins_command
from commands.dev import stats_command, broadcast_command, restart_command
from helpers.database import init_db, add_user, update_user_activity
# إعداد التسجيل
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def main():
    # تهيئة قاعدة البيانات
    await init_db()
    
    # إنشاء التطبيق
    application = Application.builder().token(Config.BOT_TOKEN).build()
    
    # إضافة معالجات الأوامر
    application.add_handler(CommandHandler("start", basic.start_command))
    application.add_handler(CommandHandler("مساعدة", basic.help_command))
    application.add_handler(CommandHandler("menu", basic.menu_command))
    
    # أوامر الموسيقى
    application.add_handler(CommandHandler("play", music.play_command))
    application.add_handler(CommandHandler("تشغيل", music.play_command))
    application.add_handler(CommandHandler("skip", music.skip_command))
    application.add_handler(CommandHandler("تخطي", music.skip_command))
    application.add_handler(CommandHandler("stop", music.stop_command))
    application.add_handler(CommandHandler("ايقاف", music.stop_command))
    
    # أوامر الألعاب
    application.add_handler(CommandHandler("games", games.games_menu))
    application.add_handler(CommandHandler("العاب", games.games_menu))
    application.add_handler(CommandHandler("كت", games.cat_command))
    application.add_handler(CommandHandler("كلب", games.dog_command))
    
    # أوامر الترفيه
    application.add_handler(CommandHandler("رفع", fun.promote_command))
    application.add_handler(CommandHandler("زواج", fun.marry_command))
    application.add_handler(CommandHandler("طلاق", fun.divorce_command))
    
    # أوامر الإدارة
    application.add_handler(CommandHandler("كتم", admin.mute_command))
    application.add_handler(CommandHandler("حظر", admin.ban_command))
    
    # أوامر المطورين
    application.add_handler(CommandHandler("stats", dev.stats_command))
    application.add_handler(CommandHandler("اذاعة", dev.broadcast_command))
    
    # بدء البوت
    print("🎵 البوت يعمل الآن!")
    await application.run_polling()

if __name__ == "__main__":
    asyncio.run(main())