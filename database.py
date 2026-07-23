import aiosqlite
from config import DATABASE_FILE

# ==========================
# Initialize Database
# ==========================

async def init_database():
    async with aiosqlite.connect(DATABASE_FILE) as db:

        await db.execute("""
        CREATE TABLE IF NOT EXISTS users (

            telegram_id INTEGER PRIMARY KEY,

            full_name TEXT,

            username TEXT,

            country TEXT,

            lesson INTEGER DEFAULT 1,

            quiz_score INTEGER DEFAULT 0,

            completed INTEGER DEFAULT 0,

            certificate_sent INTEGER DEFAULT 0,

            joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
        """)

        await db.commit()


# ==========================
# Register User
# ==========================

async def register_user(
    telegram_id,
    full_name,
    username
):

    async with aiosqlite.connect(DATABASE_FILE) as db:

        await db.execute("""

        INSERT OR IGNORE INTO users
        (
            telegram_id,
            full_name,
            username
        )

        VALUES (?, ?, ?)

        """, (
            telegram_id,
            full_name,
            username
        ))

        await db.commit()


# ==========================
# Get User
# ==========================

async def get_user(
    telegram_id
):

    async with aiosqlite.connect(DATABASE_FILE) as db:

        cursor = await db.execute("""

        SELECT *

        FROM users

        WHERE telegram_id = ?

        """, (
            telegram_id,
        ))

        return await cursor.fetchone()


# ==========================
# Update Lesson
# ==========================

async def update_lesson(
    telegram_id,
    lesson
):

    async with aiosqlite.connect(DATABASE_FILE) as db:

        await db.execute("""

        UPDATE users

        SET lesson = ?

        WHERE telegram_id = ?

        """, (
            lesson,
            telegram_id
        ))

        await db.commit()


# ==========================
# Update Quiz Score
# ==========================

async def update_score(
    telegram_id,
    score
):

    async with aiosqlite.connect(DATABASE_FILE) as db:

        await db.execute("""

        UPDATE users

        SET quiz_score = ?

        WHERE telegram_id = ?

        """, (
            score,
            telegram_id
        ))

        await db.commit()


# ==========================
# Mark Course Completed
# ==========================

async def complete_course(
    telegram_id
):

    async with aiosqlite.connect(DATABASE_FILE) as db:

        await db.execute("""

        UPDATE users

        SET completed = 1

        WHERE telegram_id = ?

        """, (
            telegram_id,
        ))

        await db.commit()


# ==========================
# Certificate Sent
# ==========================

async def certificate_sent(
    telegram_id
):

    async with aiosqlite.connect(DATABASE_FILE) as db:

        await db.execute("""

        UPDATE users

        SET certificate_sent = 1

        WHERE telegram_id = ?

        """, (
            telegram_id,
        ))

        await db.commit()
