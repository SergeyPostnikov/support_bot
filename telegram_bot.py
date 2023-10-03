import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import Updater
from helpers import detect_intent_text, TelegramLogsHandler
import logging
import telegram

logger = logging.getLogger(__file__)


def df_handle(update: Update, context: CallbackContext) -> None:
    try:
        response = detect_intent_text(
            project_id=project_id,
            session_id=12345678,
            text=update.message.text,
            language_code='ru'
        )
        update.message.reply_text(response.query_result.fulfillment_text)
    except Exception as exc:
        logger.error(f"Error in message handling: {exc}")


if __name__ == '__main__':
    load_dotenv()
    log_reciever_id = os.getenv('TG_ADMIN_ID')
    logger_bot_token = os.getenv('LOGGER_BOT_KEY')
    logger_bot = telegram.Bot(token=logger_bot_token)
    logging.basicConfig(level=logging.ERROR)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(TelegramLogsHandler(logger_bot, log_reciever_id))
    logger.info('support-bot with dialogflow started')

    bot_token = os.getenv('SUPPORT_BOT_KEY')
    project_id = os.getenv('PROJECT_ID')
    updater = Updater(token=bot_token, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, df_handle))
    updater.start_polling()
    updater.idle()
