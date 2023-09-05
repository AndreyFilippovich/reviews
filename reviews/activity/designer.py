from telegram_bot_pagination import InlineKeyboardPaginator

from db import count_of_activities, list_of_activities


def prof(data):
    return {
        'designer': 'Дизайн',
        'target': 'Таргет',
        'manager': 'Менеджмент',
        'content_manager': 'Контент-менеджер',
        'marketolog': 'Маркетолог',
        'producer': 'Продюсер',
        'blogger_manager': 'Менеджер по блогерам'
    }[data]


def prof_base(update, context, data):
    activities = prof(data)
    messages = list_of_activities(activities=activities, limit=1, offset=0)
    return '\n\n'.join([f'\nКто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),


def find_by_prof(update, context, data):
    activities = prof(data)
    
    count_messages = count_of_activities(activities=activities)

    paginator = InlineKeyboardPaginator(
        count_messages,
        data_pattern=f'{data}'+'_reviews#{page}'
    )


    update.callback_query.edit_message_text(
        text=prof_base(update, context, data)[0],
        reply_markup=paginator.markup,
        parse_mode='Markdown'
    )


def prof_reviews_callback(update, context):
    activities = prof(update.callback_query.data[:-10])
    count_messages = count_of_activities(activities=activities)
    query = update.callback_query

    query.answer()

    page = int(query.data.split('#')[1])

    paginator = InlineKeyboardPaginator(
        count_messages,
        current_page=page,
        data_pattern=f'{update.callback_query.data[:-10]}'+'_reviews#{page}'
    )

    messages = list_of_activities(activities=activities, limit=1, offset=page-1)
    query.edit_message_text(
        text = '\n\n'.join([f'\nКто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
        reply_markup=paginator.markup,
        parse_mode='Markdown'
    )