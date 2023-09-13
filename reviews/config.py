import telegram

from db import init_db

import os

from dotenv import load_dotenv

load_dotenv()
init_db()

secret_token = os.getenv('TOKEN')
secret_chat_id = os.getenv('CHAT_ID')
secret_feedback_chat_id = os.getenv('FEEDBACK_USER_ID')

bot = telegram.Bot(token=secret_token)

channel_id = os.getenv('CHANNEL_ID')

bot_url = os.getenv('URL')
