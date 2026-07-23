from telegram import (
    ReplyKeyboardMarkup,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from config import (
    SELAR_LINK,
    WHATSAPP_LINK,
    TELEGRAM_CHANNEL,
)


# ==========================
# Main Menu
# ==========================

def main_menu():

    keyboard = [

        ["📚 Start Learning", "🎯 Continue Course"],

        ["🏆 My Certificate"],

        ["💎 Join SIGC"],

        ["📢 Telegram Channel"],

        ["📞 Contact Coach"],

        ["❓ FAQ"]

    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True,
        one_time_keyboard=False
    )


# ==========================
# Continue Button
# ==========================

def continue_button():

    keyboard = [

        ["➡️ Continue"]

    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )


# ==========================
# Premium Buttons
# ==========================

def premium_buttons():

    keyboard = InlineKeyboardMarkup(

        [

            [

                InlineKeyboardButton(

                    "💎 Register on Selar",

                    url=SELAR_LINK

                )

            ],

            [

                InlineKeyboardButton(

                    "📞 Contact Coach",

                    url=WHATSAPP_LINK

                )

            ],

            [

                InlineKeyboardButton(

                    "📢 Join Telegram Channel",

                    url=TELEGRAM_CHANNEL

                )

            ]

        ]

    )

    return keyboard


# ==========================
# FAQ Button
# ==========================

def faq_button():

    keyboard = [

        ["⬅️ Back to Main Menu"]

    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )
