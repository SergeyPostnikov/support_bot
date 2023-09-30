import os

from dotenv import load_dotenv
# import telegram
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import Updater
from run import detect_intent_texts


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я бот-эхо. Просто отправь мне текст, и я отвечу тем же текстом.')


def echo(update: Update, context: CallbackContext):
    update.message.reply_text(update.message.text)


def df_handle(update: Update, context: CallbackContext) -> None:
    texts = [update.message.text]

    response = detect_intent_texts(
        project_id=project_id,
        session_id=12345678,
        texts=texts,
        language_code='ru'
    )
    update.message.reply_text(response.query_result.fulfillment_text)


if __name__ == '__main__':
    load_dotenv()
    bot_token = os.getenv('TG_TOKEN')
    project_id = os.getenv('PROJECT_ID')

    updater = Updater(token=bot_token, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, df_handle))
    updater.start_polling()
    updater.idle()
