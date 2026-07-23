import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ==========================
# Telegram Bot
# ==========================
BOT_TOKEN = os.getenv("BOT_TOKEN")

BOT_NAME = os.getenv(
    "BOT_NAME",
    "Mascot Affiliate Academy"
)

BOT_USERNAME = os.getenv(
    "BOT_USERNAME",
    "@mascotaffiliatebot"
)

# ==========================
# Coach Details
# ==========================
COACH_NAME = os.getenv(
    "COACH_NAME",
    "Coach Mascot"
)

COACH_USERNAME = os.getenv(
    "COACH_USERNAME",
    "@mascotaffiliate"
)

# ==========================
# Links
# ==========================
SELAR_LINK = os.getenv(
    "SELAR_LINK",
    "https://selar.com/p8v1233911"
)

WHATSAPP_LINK = os.getenv(
    "WHATSAPP_LINK",
    "https://wa.me/qr/5VFO46UL6FWPI1"
)

TELEGRAM_CHANNEL = os.getenv(
    "TELEGRAM_CHANNEL",
    "https://t.me/macotdigitalacademy"
)

# ==========================
# Course Settings
# ==========================
COURSE_NAME = "Affiliate Marketing Mastery for Beginners"

TOTAL_LESSONS = 30

CERTIFICATE_TITLE = (
    "Affiliate Marketing Mastery Certificate"
)

# ==========================
# Database
# ==========================
DATABASE_FILE = "data/users.db"

# ==========================
# Premium Program
# ==========================
PREMIUM_PROGRAM = (
    "Steady Income Generating Circle (SIGC)"
)

PREMIUM_PRICE = "₦1,500"
