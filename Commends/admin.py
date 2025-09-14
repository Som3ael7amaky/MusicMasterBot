from telegram import Update
from telegram.ext import CallbackContext
from helpers.database import get_db_connection

async def mute_command(update: Update, context: CallbackContext):
    if not await is_admin(update.effective_chat.id, update.effective_user.id):
        await update.message.reply_text("❌ هذا الأمر للمشرفين فقط!")
        return
    
    if not context.args:
        await update.message.reply_text("❌ يجب ذكر المستخدم لكتمه")
        return
    
    target = context.args[0]
    await update.message.reply_text(f"🔇 تم كتم {target} بنجاح!")

async def ban_command(update: Update, context: CallbackContext):
    if not await is_admin(update.effective_chat.id, update.effective_user.id):
        await update.message.reply_text("❌ هذا الأمر للمشرفين فقط!")
        return
    
    if not context.args:
        await update.message.reply_text("❌ يجب ذكر المستخدم لحظره")
        return
    
    target = context.args[0]
    await update.message.reply_text(f"🚫 تم حظر {target} بنجاح!")

async def admins_command(update: Update, context: CallbackContext):
    admins = await context.bot.get_chat_administrators(update.effective_chat.id)
    admin_list = "\n".join([f"• {admin.user.first_name}" for admin in admins])
    await update.message.reply_text(f"👮 قائمة المشرفين:\n{admin_list}")

async def is_admin(chat_id, user_id):
    try:
        chat_member = await context.bot.get_chat_member(chat_id, user_id)
        return chat_member.status in ['administrator', 'creator']
    except:
        return False