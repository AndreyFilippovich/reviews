import requests

from telegram import InlineKeyboardMarkup


from config import channel_id, bot_url
from keyboards import subscribe_keyboard, start_keyboard, SUBSCRIBE
from telegram.ext import CallbackQueryHandler

from constants.messages import FALSE_SUBSCRIBE_MESSAGE, TO_MAIN_MENU_MESSAGE


def get(url, data):
    response = requests.post(url=url, data=data)
    data = response.json()
    return data


def check_start_subscription(update, context):
    """Функция-проверки и внесения в БД нового подписчика"""
    CHANNEL_ID = channel_id
    USER_ID = update.effective_user.id
    chat = update.effective_chat
    url = bot_url
    data = {"chat_id": f"{CHANNEL_ID}", "user_id": f"{USER_ID}"}
    subscribe = get(url, data)
    if subscribe["result"]["status"] == "member":
        context.bot.send_message(chat_id=chat.id,
                                       text = TO_MAIN_MENU_MESSAGE,
                                       reply_markup = InlineKeyboardMarkup(start_keyboard)
                                       )
    elif subscribe["result"]["status"] == "left":
        context.bot.send_message(
            chat_id=chat.id,
            text=FALSE_SUBSCRIBE_MESSAGE,
            reply_markup=InlineKeyboardMarkup(subscribe_keyboard),
        )
