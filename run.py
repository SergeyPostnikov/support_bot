from google.cloud import api_keys_v2
from google.cloud.api_keys_v2 import Key
import os
from dotenv import load_dotenv
from google.cloud import dialogflow


def create_api_key(project_id: str, suffix: str) -> Key:
    """
    Creates and restrict an API key. Add the suffix for uniqueness.
    Args:
        project_id: Google Cloud project id.

    Returns:
        response: Returns the created API Key.
    """
    # Create the API Keys client.
    client = api_keys_v2.ApiKeysClient()

    key = api_keys_v2.Key()
    key.display_name = f"API key - {suffix}"

    request = api_keys_v2.CreateKeyRequest()
    request.parent = f"projects/{project_id}/locations/global"
    request.key = key
    response = client.create_key(request=request).result()

    print(f"Successfully created an API key: {response.key_string}")
    return response


def detect_intent_texts(project_id, session_id, texts, language_code):
    """Returns the result of detect intent with texts as inputs.

    Using the same `session_id` between requests allows continuation
    of the conversation."""

    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    # print("Session path: {}\n".format(session))

    for text in texts:
        text_input = dialogflow.TextInput(text=text, language_code=language_code)

        query_input = dialogflow.QueryInput(text=text_input)

        response = session_client.detect_intent(
            request={"session": session, "query_input": query_input}
        )

    return response


if __name__ == '__main__':
    load_dotenv()
    project_id = os.getenv('PROJECT_ID')
    # print(create_api_key(project_id, suffix='helper-bot-key'))

    detect_intent_texts(
        project_id=project_id,
        session_id=12345678,
        texts=['Привет'],
        language_code='ru'
    )
