from dotenv import load_dotenv
import os


if __name__ == '__main__':
    load_dotenv()
    tg_token = os.getenv('TG_TOKEN')
