import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

ALLOWED_LINK = "fvce.site"

TOKEN = os.getenv("TOKEN")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message

    if not message:
        return

    if message.new_chat_members:
        await message.delete()
        return

    if message.text:
        text = message.text.lower()

        if "http" in text or "www" in text or "t.me" in text:
            if ALLOWED_LINK not in text:
                await message.delete()

app = ApplicationBuilder().token("8285186433:AAH3XFsK7lR60WdZBWCI5m3rUKg3y3sZQy0").build()
app.add_handler(MessageHandler(filters.ALL, handle_message))

print("Bot is running...")
app.run_polling(drop_pending_updates=True)
