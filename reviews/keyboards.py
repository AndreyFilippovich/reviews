from telegram import InlineKeyboardButton
from constants.callback_data import *

manager_keyboard = [
            [InlineKeyboardButton(text='Ответить на отзыв', callback_data='feedback')],
            [InlineKeyboardButton(text='Отправить в канал', callback_data='send_to_channel')],
        ]


find_keyboard = [
    [InlineKeyboardButton('Все отзывы', callback_data='all_reviews')],
    [InlineKeyboardButton('Все мои отзывы', callback_data='my_reviews')],
    [InlineKeyboardButton('Найти по профессии', callback_data='find_by_activity')],
    [InlineKeyboardButton('Найти по имени', callback_data='find_by_name')],
]


get_activities_page_one = [
    [InlineKeyboardButton(text='Дизайн', callback_data='designer')],
    [InlineKeyboardButton(text='Таргет', callback_data='target')],
    [InlineKeyboardButton(text='Менеджмент', callback_data='manager')],
    [InlineKeyboardButton(text='Контент-менеджер', callback_data='content_manager')],
    [InlineKeyboardButton(text='Еще...', callback_data='more')],
]


get_activities_page_two = [
    [InlineKeyboardButton(text='Маркетолог', callback_data='marketolog')],
    [InlineKeyboardButton(text='Продюсер', callback_data='producer')],
    [InlineKeyboardButton(text='Менеджер по блогерам', callback_data='blogger_manager')],
    [InlineKeyboardButton(text='Назад', callback_data='back')],
]
