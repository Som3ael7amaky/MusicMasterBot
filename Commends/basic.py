import random
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext
from helpers.responses import WELCOME_MESSAGES, HELP_MESSAGES
from helpers.database import add_user, update_user_activity

async def start_command(update: Update, context: CallbackContext):
    user = update.effective_user
    # تسجيل المستخدم في قاعدة البيانات
    add_user(user.id, user.username, user.first_name, user.last_name)
    
    welcome_msg = random.choice(WELCOME_MESSAGES).format(user=user.first_name)
    # باقي الكود...
async def start_command(update: Update, context: CallbackContext):
    user = update.effective_user
    welcome_msg = random.choice(WELCOME_MESSAGES).format(user=user.first_name)
    
    keyboard = [
        ['🎵 تشغيل', '⏭️ تخطي'],
        ['⏸️ إيقاف', '▶️ استئناف'],
        ['🎮 الألعاب', '⚡ الترفيه'],
        ['⚙️ الإعدادات', 'ℹ️ المساعدة']
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    await update.message.reply_text(welcome_msg, reply_markup=reply_markup)

async def help_command(update: Update, context: CallbackContext):
    await update.message.reply_text(HELP_MESSAGES["main"], parse_mode='Markdown')