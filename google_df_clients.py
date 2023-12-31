from google.cloud import api_keys_v2
from google.cloud import dialogflow
from google.cloud.api_keys_v2 import Key

 
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


def detect_intent_text(project_id, session_id, text, language_code):
    """Returns the result of detect intent with texts as inputs.

    Using the same `session_id` between requests allows continuation
    of the conversation."""

    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    text_input = dialogflow.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.QueryInput(text=text_input)
    response = session_client.detect_intent(
        request={"session": session, "query_input": query_input}
    )
    return response
