import psutil
from telegram import Update
from telegram.ext import CallbackContext
from config import Config
from helpers.database import get_db_connection

async def stats_command(update: Update, context: CallbackContext):
    if update.effective_user.id not in Config.DEVELOPERS:
        await update.message.reply_text("❌ هذا الأمر للمطورين فقط!")
        return
    
    # إحصائيات النظام
    cpu_usage = psutil.cpu_percent()
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    
    # إحصائيات البوت
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users")
    user_count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM groups")
    group_count = cursor.fetchone()[0]
    conn.close()
    
    stats_text = f"""
📊 إحصائيات البوت:

👥 المستخدمين: {user_count}
💬 المجموعات: {group_count}
🖥️ استخدام المعالج: {cpu_usage}%
🧠 استخدام الذاكرة: {memory.percent}%
💾 استخدام التخزين: {disk.percent}%
    """
    await update.message.reply_text(stats_text)

async def broadcast_command(update: Update, context: CallbackContext):
    if update.effective_user.id not in Config.DEVELOPERS:
        await update.message.reply_text("❌ هذا الأمر للمطورين فقط!")
        return
    
    if not context.args:
        await update.message.reply_text("❌ اكتب الرسالة التي تريد بثها")
        return
    
    message = " ".join(context.args)
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT user_id FROM users")
    users = cursor.fetchall()
    conn.close()
    
    success = 0
    failed = 0
    
    for user in users:
        try:
            await context.bot.send_message(chat_id=user[0], text=f"📢 إشعار من المطور:\n\n{message}")
            success += 1
        except:
            failed += 1
    
    await update.message.reply_text(f"✅ تم البث لـ {success} مستخدم\n❌ فشل البث لـ {failed} مستخدم")

async def restart_command(update: Update, context: CallbackContext):
    if update.effective_user.id not in Config.DEVELOPERS:
        await update.message.reply_text("❌ هذا الأمر للمطورين فقط!")
        return
    
    await update.message.reply_text("🔄 جاري إعادة تشغيل البوت...")
    # كود إعادة التشغيل الفعلي يعتمد على نظام التشغيل