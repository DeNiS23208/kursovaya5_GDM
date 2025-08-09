import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

CHAT_ID_FILE = "chat_ids.txt"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    user = update.effective_user.first_name
    with open(CHAT_ID_FILE, "a") as f:
        f.write(f"{chat_id}\n")
    await context.bot.send_message(
        chat_id=chat_id, text=f"Привет, {user}! Ты подписан на напоминания."
    )


def run_bot():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Бот запущен...")
    app.run_polling()
