import os

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

# ============================================================
# CONFIGURATION
# ============================================================

BOT_TOKEN = os.environ.get("BOT_TOKEN")

MICROSOFT_ACCOUNT_URL = "https://account.microsoft.com/"
MICROSOFT_SECURITY_URL = "https://account.microsoft.com/security"
MICROSOFT_PASSWORD_URL = "https://account.microsoft.com/security"


# ============================================================
# /start
# ============================================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [
            InlineKeyboardButton(
                "🔐 Change Xbox/Microsoft Password",
                url=MICROSOFT_PASSWORD_URL
            )
        ],
        [
            InlineKeyboardButton(
                "👤 Microsoft Account",
                url=MICROSOFT_ACCOUNT_URL
            )
        ],
        [
            InlineKeyboardButton(
                "🛡️ Security",
                url=MICROSOFT_SECURITY_URL
            )
        ],
        [
            InlineKeyboardButton(
                "ℹ️ Help",
                callback_data="help"
            )
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🎮 Xbox Account Helper\n\n"
        "Manage your Xbox/Microsoft account using Microsoft's "
        "official website.\n\n"
        "🔒 IMPORTANT:\n"
        "This bot never asks for or stores your Microsoft password, "
        "recovery codes, or authentication cookies.\n\n"
        "Tap a button below to continue.",
        reply_markup=reply_markup
    )


# ============================================================
# /help
# ============================================================

async def help_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    keyboard = [
        [
            InlineKeyboardButton(
                "🔐 Change Password",
                url=MICROSOFT_PASSWORD_URL
            )
        ],
        [
            InlineKeyboardButton(
                "👤 Microsoft Account",
                url=MICROSOFT_ACCOUNT_URL
            )
        ]
    ]

    await update.message.reply_text(
        "ℹ️ Xbox Account Helper\n\n"
        "This bot provides shortcuts to official Microsoft "
        "account-management pages.\n\n"
        "Commands:\n"
        "/start — Open the main menu\n"
        "/security — Open Microsoft security\n"
        "/help — Show this help\n\n"
        "🔒 Never send your Microsoft password to a Telegram bot.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# ============================================================
# /security
# ============================================================

async def security_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    keyboard = [
        [
            InlineKeyboardButton(
                "🛡️ Open Microsoft Security",
                url=MICROSOFT_SECURITY_URL
            )
        ]
    ]

    await update.message.reply_text(
        "🛡️ Microsoft Account Security\n\n"
        "Use Microsoft's official website to manage your "
        "password and account security.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# ============================================================
# BUTTON HANDLER
# ============================================================

async def button_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query

    await query.answer()

    if query.data == "help":

        keyboard = [
            [
                InlineKeyboardButton(
                    "🔐 Change Password",
                    url=MICROSOFT_PASSWORD_URL
                )
            ],
            [
                InlineKeyboardButton(
                    "👤 Microsoft Account",
                    url=MICROSOFT_ACCOUNT_URL
                )
            ],
        ]

        await query.message.reply_text(
            "🔒 Security Information\n\n"
            "Your Microsoft credentials should only be entered "
            "on Microsoft's official website.\n\n"
            "This Telegram bot does not collect:\n"
            "• Microsoft passwords\n"
            "• Recovery codes\n"
            "• Authentication cookies\n"
            "• Two-factor authentication codes",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


# ============================================================
# ERROR HANDLER
# ============================================================

async def error_handler(
    update: object,
    context: ContextTypes.DEFAULT_TYPE
):

    print("Bot error:", context.error)


# ============================================================
# MAIN
# ============================================================

def main():

    if not BOT_TOKEN:
        raise RuntimeError(
            "BOT_TOKEN is missing. "
            "Add BOT_TOKEN to Railway Variables."
        )

    application = (
        Application.builder()
        .token(BOT_TOKEN)
        .build()
    )

    # Commands
    application.add_handler(
        CommandHandler("start", start)
    )

    application.add_handler(
        CommandHandler("help", help_command)
    )

    application.add_handler(
        CommandHandler("security", security_command)
    )

    # Buttons
    application.add_handler(
        CallbackQueryHandler(button_handler)
    )

    # Errors
    application.add_error_handler(error_handler)

    print("======================================")
    print("Xbox Telegram Bot is running...")
    print("Microsoft Account Helper")
    print("Press CTRL+C to stop.")
    print("======================================")

    application.run_polling(
        allowed_updates=Update.ALL_TYPES
    )


if __name__ == "__main__":
    main()
