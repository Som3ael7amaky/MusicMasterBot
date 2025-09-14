import sqlite3
import os
from config import Config

def get_db_connection():
    """الحصول على اتصال بقاعدة البيانات"""
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """تهيئة قاعدة البيانات"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # جدول المستخدمين
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        username TEXT,
        first_name TEXT,
        last_name TEXT,
        join_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        last_active TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    # جدول المجموعات
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS groups (
        group_id INTEGER PRIMARY KEY,
        title TEXT,
        join_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        last_active TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    # جدول الإحصائيات
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS stats (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        songs_played INTEGER DEFAULT 0,
        commands_used INTEGER DEFAULT 0,
        games_played INTEGER DEFAULT 0,
        last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    # إدراج إحصائيات أولية
    cursor.execute('INSERT OR IGNORE INTO stats (id) VALUES (1)')
    
    conn.commit()
    conn.close()
    print("✅ تم تهيئة قاعدة البيانات بنجاح")

def add_user(user_id, username, first_name, last_name):
    """إضافة مستخدم جديد إلى قاعدة البيانات"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT OR REPLACE INTO users (user_id, username, first_name, last_name, last_active)
    VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP)
    ''', (user_id, username, first_name, last_name))
    
    conn.commit()
    conn.close()

def update_user_activity(user_id):
    """تحديث وقت النشاط الأخير للمستخدم"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
    UPDATE users SET last_active = CURRENT_TIMESTAMP WHERE user_id = ?
    ''', (user_id,))
    
    conn.commit()
    conn.close()

def increment_stat(stat_name):
    """زيادة عداد إحصائي"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute(f'''
    UPDATE stats SET {stat_name} = {stat_name} + 1, last_updated = CURRENT_TIMESTAMP
    WHERE id = 1
    ''')
    
    conn.commit()
    conn.close()