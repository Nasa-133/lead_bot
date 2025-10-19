from telegram import Bot, Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
import os

# .env faylini yuklash
load_dotenv()

# Bot tokeningiz va kanal ID .env faylidan olinadi
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")


async def forward_to_channel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Kelgan har qanday xabarni kanalga yuborish"""
    try:
        # Xabarni kanalga forward qilish (eng oddiy usul)
        await update.message.forward(chat_id=CHANNEL_ID)

        # Yoki o'zingiz formatlasangiz:
        # await context.bot.send_message(
        #     chat_id=CHANNEL_ID,
        #     text=update.message.text
        # )

    except Exception as e:
        print(f"Xatolik: {e}")


# Botni ishga tushirish
app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, forward_to_channel))

print("Bot ishlayapti...")
app.run_polling()