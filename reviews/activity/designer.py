from telegram_bot_pagination import InlineKeyboardPaginator

from db import count_of_activities, list_of_activities


def designer_base(update, context, data):
    if data == 'designer':
        activities='Дизайн'
    messages = list_of_activities(activities=activities, limit=1, offset=0)
    return '\n\n'.join([f'\nКто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),


def designer_reviews(update, context, data):
    if data == 'designer':
        activities='Дизайн'
    
    count_messages = count_of_activities(activities=activities)

    paginator = InlineKeyboardPaginator(
        count_messages,
        data_pattern='designer_reviews#{page}'
    )


    update.callback_query.edit_message_text(
        text=designer_base(update, context, data)[0],
        reply_markup=paginator.markup,
        parse_mode='Markdown'
    )


def designer_reviews_callback(update, context, data):
    if data == 'designer':
        activities='Дизайн'
    count_messages = count_of_activities(activities=activities)
    query = update.callback_query

    query.answer()

    page = int(query.data.split('#')[1])

    paginator = InlineKeyboardPaginator(
        count_messages,
        current_page=page,
        data_pattern='designer_reviews#{page}'
    )

    messages = list_of_activities(activities=activities, limit=1, offset=page-1)
    query.edit_message_text(
        text = '\n\n'.join([f'\nКто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
        reply_markup=paginator.markup,
        parse_mode='Markdown'
    )