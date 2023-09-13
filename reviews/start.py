from buttons import main_button
from constants.messages import WELCOME_MESSAGE, HELP_MESSAGE

def start(update, context):
    chat = update.effective_chat
    name = update.effective_chat.first_name
    context.bot.send_message(
        chat_id=chat.id,
        text=WELCOME_MESSAGE.format(name),
        reply_markup=main_button
    )

def help(update, context):
    chat = update.effective_chat
    context.bot.send_message(
        chat_id=chat.id,
        text=HELP_MESSAGE,
        reply_markup=main_button
    )