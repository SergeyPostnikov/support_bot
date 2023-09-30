import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from dotenv import load_dotenv
import os
import random
from run import detect_intent_texts


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

        vk_api.messages.send(
            user_id=event.user_id,
            message=response.query_result.fulfillment_text,
            random_id=random.randint(1, 1000)
        )


if __name__ == '__main__':
    load_dotenv()
    vk_token = os.getenv('VK_TOKEN')    
    project_id = os.getenv('PROJECT_ID')
    vk_session = vk_api.VkApi(token=vk_token)
    vk_api = vk_session.get_api()

    longpoll = VkLongPoll(vk_session)

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            df_handle(event, vk_api, project_id)
