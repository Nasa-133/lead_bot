from telegram import Bot, Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
import os

# .env faylini yuklash
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")


async def forward_to_channel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Kelgan har qanday xabarni kanalga yuborish"""
    try:

        await update.message.forward(chat_id=CHANNEL_ID)


    except Exception as e:
        print(f"Xatolik: {e}")



app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, forward_to_channel))

print("Bot ishlayapti...")
app.run_polling()