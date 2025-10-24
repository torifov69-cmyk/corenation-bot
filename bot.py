import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler

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

def start(update: Update, context: CallbackContext) -> None:
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

    update.message.reply_text(welcome_text, reply_markup=reply_markup)

def handle_message(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("💻 Перейти в канал CoreNation", url=MAIN_CHANNEL_LINK)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(
        "Используйте /start для основного меню\n"
        "Или нажмите кнопку ниже, чтобы перейти в наш канал 👇",
        reply_markup=reply_markup
    )

def help_command(update: Update, context: CallbackContext) -> None:
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

    update.message.reply_text(help_text, reply_markup=reply_markup)

def channel_command(update: Update, context: CallbackContext) -> None:
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

    update.message.reply_text(channel_text, reply_markup=reply_markup)

def main() -> None:
    updater = Updater(BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("channel", channel_command))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    print("🤖 Бот @corenation_bot запущен на Render!")
    print("🔗 Перенаправляет пользователей в:", MAIN_CHANNEL_LINK)
    
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()