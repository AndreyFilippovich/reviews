from buttons import main_button

from keyboards import find_keyboard, get_activities_page_one, get_activities_page_two

from telegram import InlineKeyboardMarkup, Update, ReplyKeyboardRemove

from db import list_of_workers, get_all_reviews

from telegram.ext import ConversationHandler, CallbackContext


def find_review(update, context):
    update.message.reply_text(
        'Вы можете найти отзыв/ы по нескольким параметрам\n\n'
        'Выберите подходящий для вас\n\n',
        reply_markup=InlineKeyboardMarkup(find_keyboard)
        )


def all_reviews(update, context):
    context.bot.send_message(
        update.effective_chat.id,
        text='Тут вы найдёте все отзывы на всех исполнителей',
    )



def callback_handler(update: Update, context: CallbackContext):
    data = update.callback_query.data


    if data == 'all_reviews':
        context.bot.send_message(
        update.effective_chat.id,
        text='Пока закончим',
    )











def my_reviews(update, context):
    context.bot.send_message(
        update.effective_chat.id,
        text='gsdgsdgsdgg',
    )


def find_by_activity(update, context):
    update.callback_query.edit_message_text(
        text='Выберите профессию по которой хотите посмотреть отзывы на исполнителей',
        reply_markup=InlineKeyboardMarkup(get_activities_page_one)
    )

def find_by_activity_2(update, context):
    current_text = update.effective_message.text
    update.callback_query.edit_message_text(
        text=current_text,
        reply_markup=InlineKeyboardMarkup(get_activities_page_two),
    )







def find_by_name(update, context):
    context.bot.send_message(
        update.effective_chat.id,
        text='gsgEGWGdg',
    )










def facts_to_name(user_data):
    facts = list() 
    for key, value in user_data.items():
        facts.append('{}'.format(value))

    return value

WORKER_NAME = range(1)

def ask_worker_name(update, _):
    update.message.reply_text(
        'Введите имя человека, отзыв о котором хотите найти.'
    )
    return WORKER_NAME

def finish_worker_name(update, context):
    user_data = context.user_data
    category = 'Имя'
    text = update.message.text
    user_data[category] = text
    worker_name = facts_to_name(user_data)
    messages = list_of_workers(worker=worker_name, limit=5)
    if not messages:
        text = 'Пробуем дальше'
        update.effective_message.reply_text(
            text = text,
        )
    update.effective_message.reply_text(
        text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
    reply_markup = main_button,
    )
    return ConversationHandler.END