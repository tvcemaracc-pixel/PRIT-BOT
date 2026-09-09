import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Biar bisa liat log di Railway
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Ambil TOKEN dari Railway Variables biar aman
TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Halo Raja! 👋\n\n"
        "Bot Monitor Lapangan Gambut KKR udah online ✅\n\n"
        "Perintah:\
