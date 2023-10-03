# Support Bots for VK and Telegram

## Overview
This project consists of support bots for VK (VKontakte) and Telegram messaging platforms. These bots are designed to provide support to users in a group on VK and a channel on Telegram using the Dialogflow natural language understanding platform.


<img src="https://dvmn.org/filer/canonical/1569214094/323/" width="35%" />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://dvmn.org/filer/canonical/1569214089/322/" width="35%" /> 


## Prerequisites
Before you can run the support bots, you will need the following tokens and identifiers:

- `SUPPORT_BOT_KEY`: Telegram Bot Token
- `PROJECT_ID`: Google Cloud Project ID
- `GC_API_KEY`: Google Cloud API Key (for Dialogflow integration)
- `VK_TOKEN`: VKontakte Community Token
- `GOOGLE_APPLICATION_CREDENTIALS`: Google Application Credentials JSON file path (for Google Cloud services)

- `LOGGER_BOT_KEY`: Your crush reporter bot token
- `TG_ADMIN_ID`: Your id for recieving crush reports

Make sure to obtain these tokens and identifiers from the respective platforms and services.

## Installation
1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/SergeyPostnikov/support-bot.git
    ```

2. Install the required Python libraries by running:

    ```bash
    pip install -r requirements.txt
    ```

## Configuration
Edit the configuration files or environment variables with your tokens and identifiers:

- For VK bot, update `VK_TOKEN` in the VK configuration file.
- For Telegram bot, set `TG_TOKEN` in the Telegram configuration file.
- Set `PROJECT_ID` and `GC_API_KEY` for Dialogflow integration.

## Usage
1. Run the VK support bot:

    ```bash
    python vk_bot.py
    ```

2. Run the Telegram support bot:

    ```bash
    python telegram_bot.py
    ```

3. Your bots are now active and ready to provide support in your VK group and Telegram channel.

## add_intent.py
These bots use Dialogflow for natural language understanding and responses. Make sure you have configured Dialogflow intents and entities to handle user queries effectively. The 'add_intent.py' is a Python script that enables the creation of intents in Google Cloud Dialogflow from a JSON file containing questions and answers. This script is particularly useful for setting up responses to common user queries in your chatbot or virtual assistant.

## Prerequisites

- `Google Cloud SDK`: Installed and authenticated.
- `Dialogflow` Agent: Set up in your Google Cloud project.
- `JSON File`: A JSON file containing the questions and answers you wish to use for intents.

for usage create a JSON file (e.g., questions.json) containing the intents and their corresponding questions and answers in the following format:
```
{
    "Intent Name 1": {
        "questions": [
            "Question 1",
            "Question 2",
            ...
        ],
        "answer": "Answer to Intent 1"
    },
    "Intent Name 2": {
        "questions": [
            "Question 1",
            "Question 2",
            ...
        ],
        "answer": "Answer to Intent 2"
    },
    ...
}

```
### Usage:

```bash
python3 add_intents.py [--json_path questions.json]
```
--json_path (optional): Path to the JSON file containing intents. The default is questions.json in the script's directory.

## Google Cloud Services
The `GOOGLE_APPLICATION_CREDENTIALS` environment variable should point to your Google Cloud service account key JSON file. Ensure it is correctly set up to enable Google Cloud service integration.

## Contributing
Feel free to contribute to this project by opening issues or submitting pull requests. Your contributions are highly appreciated!

## Project Goals
This project was created for educational purposes, aiming to demonstrate the integration of Google Cloud DialogFlow with both VK and Telegram bots.