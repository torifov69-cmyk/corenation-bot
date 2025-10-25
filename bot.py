import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Получаем токен из переменных окружения Render
BOT_TOKEN = os.environ.get('BOT_TOKEN')
MAIN_CHANNEL_LINK = "https://t.me/+T2xIp-BByFYzYWNi"

if not BOT_TOKEN:
    logging.error("BOT_TOKEN not set!")
    exit(1)

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("💻 Перейти в канал CoreNation", url=MAIN_CHANNEL_LINK)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    welcome_text = (
        "👋 Привет!\n\n"
        "Добро пожаловать в **CoreNation Bot**!\n"
        "Этот бот перенаправляет в наш основной канал с эксклюзивным контентом!\n\n"
        "Нажми кнопку ниже, чтобы перейти в канал 👇"
    )

    await update.message.reply_text(welcome_text, reply_markup=reply_markup)

async def handle_message(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("💻 Перейти в канал CoreNation", url=MAIN_CHANNEL_LINK)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Используйте /start для основного меню\n"
        "Или нажмите кнопку ниже, чтобы перейти в наш канал 👇",
        reply_markup=reply_markup
    )

async def help_command(update: Update, context: CallbackContext) -> None:
    help_text = (
        "🤖 CoreNation Bot - перенаправитель в канал\n\n"
        "Доступные команды:\n"
        "/start - Начать работу с ботом\n"
        "/help - Показать эту справку\n"
        "/channel - Информация о канале\n\n"
        "Основной функционал доступен через кнопки меню."
    )

    keyboard = [
        [InlineKeyboardButton("💻 Перейти в канал", url=MAIN_CHANNEL_LINK)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(help_text, reply_markup=reply_markup)

async def channel_command(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("💻 Перейти в канал CoreNation", url=MAIN_CHANNEL_LINK)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    channel_text = (
        "💻 **CoreNation With Love**\n\n"
        "Присоединяйтесь к нашему каналу с любовью!\n"
        "Эксклюзивный контент, вдохновение и многое другое.\n\n"
        "Подписывайтесь и будьте частью нашего сообщества! 👇"
    )

    await update.message.reply_text(channel_text, reply_markup=reply_markup)

def main() -> None:
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("channel", channel_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Бот @corenation_bot запущен на Render!")
    print("🔗 Перенаправляет пользователей в:", MAIN_CHANNEL_LINK)
    application.run_polling()

if __name__ == "__main__":
    main()