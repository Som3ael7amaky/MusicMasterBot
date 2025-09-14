import random
import requests
from telegram import Update
from telegram.ext import CallbackContext
from config import Config

JOKES = [
    "ليش الطيور ما بتعرف تسبح؟ عشان ماعندها شبشب!",
    "مرة واحد غبي ناطح جدار وقال: ياه الجدار طالع!",
    "مرة واحد بلع بذرة بطيخ..طلعله بطيخة في دماغه..يبيعها بـ10 جنيه",
]

async def games_menu(update: Update, context: CallbackContext):
    menu_text = """
🎮 قائمة الألعاب المتاحة:

🎲 /نرد - لعبة النرد
🏀 /سلة - لعبة كرة السلة
🎯 /هدف - لعبة التسديد
🐱 /كت - صور قطط عشوائية
🐶 /كلب - صور كلاب عشوائية
😂 /نكتة - نكتة عشوائية
    """
    await update.message.reply_text(menu_text)

async def cat_command(update: Update, context: CallbackContext):
    try:
        response = requests.get("https://api.thecatapi.com/v1/images/search")
        photo_url = response.json()[0]['url']
        await update.message.reply_photo(photo_url, caption="🐱 هاك صورة قطوة جميلة!")
    except:
        await update.message.reply_text("❌ ماقدرش أجيب صورة قطوة الآن!")

async def joke_command(update: Update, context: CallbackContext):
    joke = random.choice(JOKES)
    await update.message.reply_text(f"😂 {joke}")