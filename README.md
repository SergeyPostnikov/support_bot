# Support Bots for VK and Telegram

## Overview
This project consists of support bots for VK (VKontakte) and Telegram messaging platforms. These bots are designed to provide support to users in a group on VK and a channel on Telegram using the Dialogflow natural language understanding platform.

## Prerequisites
Before you can run the support bots, you will need the following tokens and identifiers:

- `TG_TOKEN`: Telegram Bot Token
- `PROJECT_ID`: Google Cloud Project ID
- `GC_API_KEY`: Google Cloud API Key (for Dialogflow integration)
- `VK_TOKEN`: VKontakte Community Token

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

## Dialogflow Integration
These bots use Dialogflow for natural language understanding and responses. Make sure you have configured Dialogflow intents and entities to handle user queries effectively.

## Contributing
Feel free to contribute to this project by opening issues or submitting pull requests. Your contributions are highly appreciated!

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
