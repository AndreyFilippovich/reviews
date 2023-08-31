from buttons import main_button

from keyboards import find_keyboard, get_activities_page_one, get_activities_page_two

from telegram import InlineKeyboardMarkup

from db import (list_of_workers, count_of_users_messages, list_of_user_messages,
                count_of_all_messages, list_of_all_messages)

from telegram.ext import ConversationHandler
from telegram_bot_pagination import InlineKeyboardPaginator



def find_review(update, context):
    update.message.reply_text(
        'Вы можете найти отзыв/ы по нескольким параметрам\n\n'
        'Выберите подходящий для вас\n\n',
        reply_markup=InlineKeyboardMarkup(find_keyboard)
        )

# ----------------- Выдача отзывов, которые оставил пользователь -----------------

def my_reviews_base(update, context):
    user = update.effective_user.id
    count_messages = count_of_users_messages(user_id=user)
    messages = list_of_user_messages(user_id=user, limit=1, offset=0)
    return '\n\n'.join([f'Вы написали всего {count_messages} отзывов \nКто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),


def my_reviews(update, context):
    user = update.effective_user.id
    count_messages = count_of_users_messages(user_id=user)

    paginator = InlineKeyboardPaginator(
        count_messages,
        data_pattern='reviews#{page}'
    )


    update.callback_query.edit_message_text(
        text=my_reviews_base(update, context)[0],
        reply_markup=paginator.markup,
        parse_mode='Markdown'
    )


def my_reviews_callback(update, context):
    user = update.effective_user.id
    count_messages = count_of_users_messages(user_id=user)
    query = update.callback_query

    query.answer()

    page = int(query.data.split('#')[1])

    paginator = InlineKeyboardPaginator(
        count_messages,
        current_page=page,
        data_pattern='reviews#{page}'
    )

    messages = list_of_user_messages(user_id=user, limit=1, offset=page-1)
    query.edit_message_text(
        text = '\n\n'.join([f'Вы написали всего {count_messages} отзывов \nКто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
        reply_markup=paginator.markup,
        parse_mode='Markdown'
    )

# ----------------- Выдача всех отзывов пользователей -----------------


def all_reviews_base(update, context):
    count_messages = count_of_all_messages()
    messages = list_of_all_messages(limit=1, offset=0)
    return '\n\n'.join([f'Всего написано {count_messages} отзывов \nКто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),


def all_reviews(update, context):
    count_messages = count_of_all_messages()

    paginator = InlineKeyboardPaginator(
        count_messages,
        data_pattern='all_reviews#{page}'
    )


    update.callback_query.edit_message_text(
        text=all_reviews_base(update, context)[0],
        reply_markup=paginator.markup,
        parse_mode='Markdown'
    )


def all_reviews_callback(update, context):
    count_messages = count_of_all_messages()
    query = update.callback_query

    query.answer()

    page = int(query.data.split('#')[1])

    paginator = InlineKeyboardPaginator(
        count_messages,
        current_page=page,
        data_pattern='all_reviews#{page}'
    )

    messages = list_of_all_messages(limit=1, offset=page-1)
    query.edit_message_text(
        text = '\n\n'.join([f'Всего написано {count_messages} отзывов \nКто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
        reply_markup=paginator.markup,
        parse_mode='Markdown'
    )

# ----------------- Поиск отзывов по профессии -----------------

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


'designer'
'target'
'manager'
'content_manager'
'marketolog'
'producer'
'blogger_manager'


# ----------------- Поиск отзывов по имени -----------------

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