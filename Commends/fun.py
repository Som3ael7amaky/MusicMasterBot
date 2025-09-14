import random
from telegram import Update
from telegram.ext import CallbackContext
from helpers.responses import FUNNY_RESPONSES

async def promote_command(update: Update, context: CallbackContext):
    if not context.args:
        await update.message.reply_text("❌ مين اللي عايز ترفعه؟")
        return
    
    target = " ".join(context.args)
    funny_response = random.choice(FUNNY_RESPONSES)
    await update.message.reply_text(f"{funny_response}\n🎉 تم رفع {target} إلى رتبة مشرف!")

async def marry_command(update: Update, context: CallbackContext):
    if not context.args:
        await update.message.reply_text("❌ مين اللي عايز تتجوزه؟")
        return
    
    target = " ".join(context.args)
    await update.message.reply_text(f"💍 مبروك! اتجوزت {target} وخلاص بقيتوا متجوزين!")

async def divorce_command(update: Update, context: CallbackContext):
    if not context.args:
        await update.message.reply_text("❌ مين اللي عايز تطلقه؟")
        return
    
    target = " ".join(context.args)
    await update.message.reply_text(f"💔 للأسف! طلقت {target} وخلاص بقيتوا مطلقين!")