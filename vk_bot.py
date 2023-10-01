import logging
import os
import random
import telegram
import time
import vk_api

from dotenv import load_dotenv
from helpers import TelegramLogsHandler
from helpers import detect_intent_texts
from requests.exceptions import ConnectionError
from vk_api.longpoll import VkEventType
from vk_api.longpoll import VkLongPoll
from vk_api.exceptions import VkApiError

logger = logging.getLogger(__file__)


def df_handle(event, vk_api, project_id):
    user_message = event.text
    if user_message:
        language_code = 'ru'  
        response = detect_intent_texts(
            project_id, 
            event.user_id, 
            [user_message], 
            language_code
        )

        if response.query_result.intent.is_fallback:
            return

        vk_api.messages.send(
            user_id=event.user_id,
            message=response.query_result.fulfillment_text,
            random_id=random.randint(1, 1000)
        )


if __name__ == '__main__':
    load_dotenv()

    log_reciever_id = os.getenv('TG_ADMIN_ID')
    logger_bot_token = os.getenv('LOGGER_BOT_KEY')
    logger_bot = telegram.Bot(token=logger_bot_token)
    logging.basicConfig(level=logging.ERROR)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(TelegramLogsHandler(logger_bot, log_reciever_id))
    logger.info('vk helper df-bot started')

    vk_token = os.getenv('VK_TOKEN')    
    project_id = os.getenv('PROJECT_ID')
    try:
        vk_session = vk_api.VkApi(token=vk_token)
        vk_api = vk_session.get_api()
        longpoll = VkLongPoll(vk_session)

        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                df_handle(event, vk_api, project_id)
                
    except VkApiError as err:
        logging.error(f"Vk api error: {err}")
    except ConnectionError as err:
        logging.exception(err)
        time.sleep(30)
    except Exception as exc:
        logger.error(f"Bot error: {exc}")
