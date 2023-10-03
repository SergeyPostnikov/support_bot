import argparse
import json
import os

from dotenv import load_dotenv
from google.cloud import dialogflow


def create_intent_from_json(project_id, json_file_path):
    intents_client = dialogflow.IntentsClient()

    with open(json_file_path, "r", encoding='UTF-8') as json_file:
        intents = json.load(json_file)

    for intent_name, intent_value in intents.items():
        questions = intent_value["questions"]
        answer = intent_value["answer"]

        parent = dialogflow.AgentsClient.agent_path(project_id)
        training_phrases = []

        for question in questions:
            part = dialogflow.Intent.TrainingPhrase.Part(text=question)
            training_phrase = dialogflow.Intent.TrainingPhrase(parts=[part])
            training_phrases.append(training_phrase)

        text = dialogflow.Intent.Message.Text(text=[answer])
        message = dialogflow.Intent.Message(text=text)

        intent = dialogflow.Intent(
            display_name=intent_name, 
            training_phrases=training_phrases, 
            messages=[message]
        )

        response = intents_client.create_intent(
            request={"parent": parent, "intent": intent}
        )

        print(f"Intent '{intent_name}' created: {response}")


def get_arguments():
    parser = argparse.ArgumentParser(
        prog='intent learner',
        epilog='usage: add_intents.py [--json_path questions.json]',
    )
    
    parser.add_argument(
        '--json_path',
        help='Path where questions.json placed',
        default='questions.json'
    )
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = get_arguments()
    load_dotenv()
    project_id = os.getenv('PROJECT_ID')
    create_intent_from_json(project_id, args.json_path)
