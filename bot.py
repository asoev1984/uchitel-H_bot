import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Токен бота
TOKEN = "7470843946:AAEtXKGlQOM6hL4jdv-SkxG46e869xAV724"

# ID группы, откуда документы (если нужно)
GROUP_ID = -1001234567890

# Список документов (замени на свои данные)
documents = [
    {"name": "План работы", "url": "https://example.com/plan.pdf"},
    {"name": "График дежурств", "url": "https://example.com/schedule.pdf"},
    {"name": "Методичка", "url": "https://example.com/method.pdf"},
]

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton(doc["name"], url=doc["url"])] for doc in documents]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Выберите документ:", reply_markup=reply_markup)

# Запуск бота
async def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    await app.run_polling()

if name == "main":
    import asyncio
    asyncio.run(main())