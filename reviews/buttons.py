from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup

from telegram import Update

from telegram.ext import CallbackContext

from main import main_button, ask_worker_name

from db import *

COMMAND_NAME = 'name'
COMMAND_LIST = 'list'
COMMAND_ACTIVITY = 'choose'

def get_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Найти по имени', callback_data=COMMAND_NAME),
            ],
            [
                InlineKeyboardButton(text='Мои сообщения', callback_data=COMMAND_LIST),
            ],
            [
                InlineKeyboardButton(text='Найти по профессии', callback_data=COMMAND_ACTIVITY),
            ],
        ]
    )

COMMAND_DESIGN = 'designer'
COMMAND_TARGET = 'target'
COMMAND_MANAGER = 'manager'
COMMAND_CONTENT_MANAGER = 'content_manager'
COMMAND_VIDEOGRAPH = 'videograph'
COMMAND_PHOTOGRAPHER = 'photographer'
COMMAND_COPYWRITER = 'copywriter'
COMMAND_MORE = 'more'

def get_activities_page_one():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Дизайн', callback_data=COMMAND_DESIGN),
            ],
            [
                InlineKeyboardButton(text='Таргет', callback_data=COMMAND_TARGET),
            ],
            [
                InlineKeyboardButton(text='Менеджмент', callback_data=COMMAND_MANAGER),
            ],
            [
                InlineKeyboardButton(text='Контент-менеджер', callback_data=COMMAND_CONTENT_MANAGER),
            ],
            [
                InlineKeyboardButton(text='Видеограф', callback_data=COMMAND_VIDEOGRAPH),
            ],
            [
                InlineKeyboardButton(text='Фотограф', callback_data=COMMAND_PHOTOGRAPHER),
            ],
            [
                InlineKeyboardButton(text='Копирайтер', callback_data=COMMAND_COPYWRITER),
            ],
            [
                InlineKeyboardButton(text='Еще...', callback_data=COMMAND_MORE),
            ],
        ],
    )

COMMAND_KONTEKSTOLOG = 'kontekstolog'
COMMAND_AVITOLOG = 'avitolog'
COMMAND_SMM = 'SMM'
COMMAND_CHAT_BOTY ='chat-bots'
COMMAND_CONTENT_MAKER ='content_maker'
COMMAND_MARKETOLOG = 'marketolog'
COMMAND_PRODUCER = 'producer'
COMMAND_BLOGGER_MANAGER = 'blogger manager'
COMMAND_BACK = 'back'

def get_activities_page_two():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Контекстная реклама', callback_data=COMMAND_KONTEKSTOLOG),
            ],
            [
                InlineKeyboardButton(text='Авитолог', callback_data=COMMAND_AVITOLOG),
            ],
            [
                InlineKeyboardButton(text='SMM-щик', callback_data=COMMAND_SMM),
            ],
            [
                InlineKeyboardButton(text='Разработчик чат-ботов', callback_data=COMMAND_CHAT_BOTY),
            ],
            [
                InlineKeyboardButton(text='Контент-мейкер', callback_data=COMMAND_CONTENT_MAKER),
            ],
            [
                InlineKeyboardButton(text='Маркетолог', callback_data=COMMAND_MARKETOLOG),
            ],
            [
                InlineKeyboardButton(text='Продюсер', callback_data=COMMAND_PRODUCER),
            ],
            [
                InlineKeyboardButton(text='Менеджер по блогерам', callback_data=COMMAND_BLOGGER_MANAGER),
            ],
            [
                InlineKeyboardButton(text='Назад', callback_data=COMMAND_BACK),
            ],
        ],
    )


'''Инлайн кнопки для пагинации запросов по дизайнерам'''


COMMAND_DESIGN_2 = 'designer_2'

def get_designers_page_two():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Вперёд --->', callback_data=COMMAND_DESIGN_2),
            ],
        ],
    )

COMMAND_DESIGN_2_MORE = 'designer_2_more'
COMMAND_DESIGN_2_BACK = 'designer_2_back'

def designers_page_2():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<--- Назад', callback_data=COMMAND_DESIGN_2_BACK),
                InlineKeyboardButton(text='Вперёд --->', callback_data=COMMAND_DESIGN_2_MORE),
            ],
        ],
    )

COMMAND_DESIGN_3_MORE = 'designer_3_more'
COMMAND_DESIGN_3_BACK = 'designer_3_back'

def designers_page_3():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<--- Назад', callback_data=COMMAND_DESIGN_3_BACK),
                InlineKeyboardButton(text='Вперёд --->', callback_data=COMMAND_DESIGN_3_MORE),
            ],
        ],
    )

COMMAND_DESIGN_4_MORE = 'designer_4_more'
COMMAND_DESIGN_4_BACK = 'designer_4_back'

def designers_page_4():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<--- Назад', callback_data=COMMAND_DESIGN_4_BACK),
                InlineKeyboardButton(text='Вперёд --->', callback_data=COMMAND_DESIGN_4_MORE),
            ],
        ],
    )

COMMAND_DESIGN_5_BACK = 'designer_5_back'

def designers_page_5():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<--- Назад', callback_data=COMMAND_DESIGN_5_BACK),
            ],
        ],
    )

'''Инлайн кнопки для пагинации запросов по таргетологам'''


COMMAND_TARGET_2 = 'target_2'

def get_target_page_two():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Вперёд --->', callback_data=COMMAND_TARGET_2),
            ],
        ],
    )

COMMAND_TARGET_2_MORE = 'target_2_more'
COMMAND_TARGET_2_BACK = 'target_2_back'

def target_page_2():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<--- Назад', callback_data=COMMAND_TARGET_2_BACK),
                InlineKeyboardButton(text='Вперёд --->', callback_data=COMMAND_TARGET_2_MORE),
            ],
        ],
    )

COMMAND_TARGET_3_MORE = 'target_3_more'
COMMAND_TARGET_3_BACK = 'target_3_back'

def target_page_3():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<--- Назад', callback_data=COMMAND_TARGET_3_BACK),
                InlineKeyboardButton(text='Вперёд --->', callback_data=COMMAND_TARGET_3_MORE),
            ],
        ],
    )

COMMAND_TARGET_4_MORE = 'target_4_more'
COMMAND_TARGET_4_BACK = 'target_4_back'

def target_page_4():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<--- Назад', callback_data=COMMAND_TARGET_4_BACK),
                InlineKeyboardButton(text='Вперёд --->', callback_data=COMMAND_TARGET_4_MORE),
            ],
        ],
    )

COMMAND_TARGET_5_BACK = 'target_5_back'

def target_page_5():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<--- Назад', callback_data=COMMAND_TARGET_5_BACK),
            ],
        ],
    )


'''Инлайн кнопки для пагинации запросов по менеджерам'''


COMMAND_MANAGER_2 = 'manager_2'

def get_manager_page_two():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Вперёд --->', callback_data=COMMAND_MANAGER_2),
            ],
        ],
    )

COMMAND_MANAGER_2_MORE = 'manager_2_more'
COMMAND_MANAGER_2_BACK = 'manager_2_back'

def manager_page_2():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<--- Назад', callback_data=COMMAND_MANAGER_2_BACK),
                InlineKeyboardButton(text='Вперёд --->', callback_data=COMMAND_MANAGER_2_MORE),
            ],
        ],
    )

COMMAND_MANAGER_3_MORE = 'manager_3_more'
COMMAND_MANAGER_3_BACK = 'manager_3_back'

def manager_page_3():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<--- Назад', callback_data=COMMAND_MANAGER_3_BACK),
                InlineKeyboardButton(text='Вперёд --->', callback_data=COMMAND_MANAGER_3_MORE),
            ],
        ],
    )

COMMAND_MANAGER_4_MORE = 'manager_4_more'
COMMAND_MANAGER_4_BACK = 'manager_4_back'

def manager_page_4():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<--- Назад', callback_data=COMMAND_MANAGER_4_BACK),
                InlineKeyboardButton(text='Вперёд --->', callback_data=COMMAND_MANAGER_4_MORE),
            ],
        ],
    )

COMMAND_MANAGER_5_BACK = 'manager_5_back'

def manager_page_5():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<--- Назад', callback_data=COMMAND_MANAGER_5_BACK),
            ],
        ],
    )


'''Инлайн кнопки для пагинации запросов по контент-менеджерам'''


COMMAND_CONTENT_MANAGER_2 = 'content_manager_2'

def get_content_manager_page_two():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Вперёд --->', callback_data=COMMAND_CONTENT_MANAGER_2),
            ],
        ],
    )

COMMAND_CONTENT_MANAGER_2_MORE = 'content_manager_2_more'
COMMAND_CONTENT_MANAGER_2_BACK = 'content_manager_2_back'

def content_manager_page_2():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<--- Назад', callback_data=COMMAND_CONTENT_MANAGER_2_BACK),
                InlineKeyboardButton(text='Вперёд --->', callback_data=COMMAND_CONTENT_MANAGER_2_MORE),
            ],
        ],
    )

COMMAND_CONTENT_MANAGER_3_MORE = 'content_manager_3_more'
COMMAND_CONTENT_MANAGER_3_BACK = 'content_manager_3_back'

def content_manager_page_3():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<--- Назад', callback_data=COMMAND_CONTENT_MANAGER_3_BACK),
                InlineKeyboardButton(text='Вперёд --->', callback_data=COMMAND_CONTENT_MANAGER_3_MORE),
            ],
        ],
    )

COMMAND_CONTENT_MANAGER_4_MORE = 'content_manager_4_more'
COMMAND_CONTENT_MANAGER_4_BACK = 'content_manager_4_back'

def content_manager_page_4():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<--- Назад', callback_data=COMMAND_CONTENT_MANAGER_4_BACK),
                InlineKeyboardButton(text='Вперёд --->', callback_data=COMMAND_CONTENT_MANAGER_4_MORE),
            ],
        ],
    )

COMMAND_CONTENT_MANAGER_5_BACK = 'content_manager_5_back'

def content_manager_page_5():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<--- Назад', callback_data=COMMAND_CONTENT_MANAGER_5_BACK),
            ],
        ],
    )


'''Инлайн кнопки для пагинации запросов по видеографам'''


COMMAND_VIDEOGRAPH_2 = 'videograph_2'

def get_videograph_page_two():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Вперёд --->', callback_data=COMMAND_VIDEOGRAPH_2),
            ],
        ],
    )

COMMAND_VIDEOGRAPH_2_MORE = 'videograph_2_more'
COMMAND_VIDEOGRAPH_2_BACK = 'videograph_2_back'

def videograph_page_2():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<--- Назад', callback_data=COMMAND_VIDEOGRAPH_2_BACK),
                InlineKeyboardButton(text='Вперёд --->', callback_data=COMMAND_VIDEOGRAPH_2_MORE),
            ],
        ],
    )

COMMAND_VIDEOGRAPH_3_MORE = 'videograph_3_more'
COMMAND_VIDEOGRAPH_3_BACK = 'videograph_3_back'

def videograph_page_3():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<--- Назад', callback_data=COMMAND_VIDEOGRAPH_3_BACK),
                InlineKeyboardButton(text='Вперёд --->', callback_data=COMMAND_VIDEOGRAPH_3_MORE),
            ],
        ],
    )

COMMAND_VIDEOGRAPH_4_MORE = 'videograph_4_more'
COMMAND_VIDEOGRAPH_4_BACK = 'videograph_4_back'

def videograph_page_4():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<--- Назад', callback_data=COMMAND_VIDEOGRAPH_4_BACK),
                InlineKeyboardButton(text='Вперёд --->', callback_data=COMMAND_VIDEOGRAPH_4_MORE),
            ],
        ],
    )

COMMAND_VIDEOGRAPH_5_BACK = 'videograph_5_back'

def videograph_page_5():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<--- Назад', callback_data=COMMAND_VIDEOGRAPH_5_BACK),
            ],
        ],
    )


'''Инлайн кнопки для пагинации запросов по фотографам'''


COMMAND_PHOTOGRAPHER_2 = 'photographer_2'

def get_photographer_page_two():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Вперёд --->', callback_data=COMMAND_PHOTOGRAPHER_2),
            ],
        ],
    )

COMMAND_PHOTOGRAPHER_2_MORE = 'photographer_2_more'
COMMAND_PHOTOGRAPHER_2_BACK = 'photographer_2_back'

def photographer_page_2():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<--- Назад', callback_data=COMMAND_PHOTOGRAPHER_2_BACK),
                InlineKeyboardButton(text='Вперёд --->', callback_data=COMMAND_PHOTOGRAPHER_2_MORE),
            ],
        ],
    )

COMMAND_PHOTOGRAPHER_3_MORE = 'photographer_3_more'
COMMAND_PHOTOGRAPHER_3_BACK = 'photographer_3_back'

def photographer_page_3():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<--- Назад', callback_data=COMMAND_PHOTOGRAPHER_3_BACK),
                InlineKeyboardButton(text='Вперёд --->', callback_data=COMMAND_PHOTOGRAPHER_3_MORE),
            ],
        ],
    )

COMMAND_PHOTOGRAPHER_4_MORE = 'photographer_4_more'
COMMAND_PHOTOGRAPHER_4_BACK = 'photographer_4_back'

def photographer_page_4():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<--- Назад', callback_data=COMMAND_PHOTOGRAPHER_4_BACK),
                InlineKeyboardButton(text='Вперёд --->', callback_data=COMMAND_PHOTOGRAPHER_4_MORE),
            ],
        ],
    )

COMMAND_PHOTOGRAPHER_5_BACK = 'photographer_5_back'

def photographer_page_5():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<--- Назад', callback_data=COMMAND_PHOTOGRAPHER_5_BACK),
            ],
        ],
    )


'''Инлайн кнопки для пагинации запросов по копирайтерам'''


COMMAND_COPYWRITER_2 = 'copywriter_2'

def get_copywriter_page_two():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Вперёд --->', callback_data=COMMAND_COPYWRITER_2),
            ],
        ],
    )

COMMAND_COPYWRITER_2_MORE = 'copywriter_2_more'
COMMAND_COPYWRITER_2_BACK = 'copywriter_2_back'

def copywriter_page_2():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<--- Назад', callback_data=COMMAND_COPYWRITER_2_BACK),
                InlineKeyboardButton(text='Вперёд --->', callback_data=COMMAND_COPYWRITER_2_MORE),
            ],
        ],
    )

COMMAND_COPYWRITER_3_MORE = 'copywriter_3_more'
COMMAND_COPYWRITER_3_BACK = 'copywriter_3_back'

def copywriter_page_3():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<--- Назад', callback_data=COMMAND_COPYWRITER_3_BACK),
                InlineKeyboardButton(text='Вперёд --->', callback_data=COMMAND_COPYWRITER_3_MORE),
            ],
        ],
    )

COMMAND_COPYWRITER_4_MORE = 'copywriter_4_more'
COMMAND_COPYWRITER_4_BACK = 'copywriter_4_back'

def copywriter_page_4():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<--- Назад', callback_data=COMMAND_COPYWRITER_4_BACK),
                InlineKeyboardButton(text='Вперёд --->', callback_data=COMMAND_COPYWRITER_4_MORE),
            ],
        ],
    )

COMMAND_COPYWRITER_5_BACK = 'copywriter_5_back'

def copywriter_page_5():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<--- Назад', callback_data=COMMAND_COPYWRITER_5_BACK),
            ],
        ],
    )



'''Инлайн кнопки для пагинации запросов по контекстологам'''


COMMAND_KONTEKSTOLOG_2 = 'kontekstolog_2'

def get_kontekstolog_page_two():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Вперёд --->', callback_data=COMMAND_KONTEKSTOLOG_2),
            ],
        ],
    )

COMMAND_KONTEKSTOLOG_2_MORE = 'kontekstolog_2_more'
COMMAND_KONTEKSTOLOG_2_BACK = 'kontekstolog_2_back'

def kontekstolog_page_2():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<--- Назад', callback_data=COMMAND_KONTEKSTOLOG_2_BACK),
                InlineKeyboardButton(text='Вперёд --->', callback_data=COMMAND_KONTEKSTOLOG_2_MORE),
            ],
        ],
    )

COMMAND_KONTEKSTOLOG_3_MORE = 'kontekstolog_3_more'
COMMAND_KONTEKSTOLOG_3_BACK = 'kontekstolog_3_back'

def kontekstolog_page_3():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<--- Назад', callback_data=COMMAND_KONTEKSTOLOG_3_BACK),
                InlineKeyboardButton(text='Вперёд --->', callback_data=COMMAND_KONTEKSTOLOG_3_MORE),
            ],
        ],
    )

COMMAND_KONTEKSTOLOG_4_MORE = 'kontekstolog_4_more'
COMMAND_KONTEKSTOLOG_4_BACK = 'kontekstolog_4_back'

def kontekstolog_page_4():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<--- Назад', callback_data=COMMAND_KONTEKSTOLOG_4_BACK),
                InlineKeyboardButton(text='Вперёд --->', callback_data=COMMAND_KONTEKSTOLOG_4_MORE),
            ],
        ],
    )

COMMAND_KONTEKSTOLOG_5_BACK = 'kontekstolog_5_back'

def kontekstolog_page_5():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<--- Назад', callback_data=COMMAND_KONTEKSTOLOG_5_BACK),
            ],
        ],
    )


'''Инлайн кнопки для пагинации запросов по авитологам'''


COMMAND_AVITOLOG_2 = 'avitolog_2'

def get_avitolog_page_two():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Вперёд --->', callback_data=COMMAND_AVITOLOG_2),
            ],
        ],
    )

COMMAND_AVITOLOG_2_MORE = 'avitolog_2_more'
COMMAND_AVITOLOG_2_BACK = 'avitolog_2_back'

def avitolog_page_2():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<--- Назад', callback_data=COMMAND_AVITOLOG_2_BACK),
                InlineKeyboardButton(text='Вперёд --->', callback_data=COMMAND_AVITOLOG_2_MORE),
            ],
        ],
    )

COMMAND_AVITOLOG_3_MORE = 'avitolog_3_more'
COMMAND_AVITOLOG_3_BACK = 'avitolog_3_back'

def avitolog_page_3():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<--- Назад', callback_data=COMMAND_AVITOLOG_3_BACK),
                InlineKeyboardButton(text='Вперёд --->', callback_data=COMMAND_AVITOLOG_3_MORE),
            ],
        ],
    )

COMMAND_AVITOLOG_4_MORE = 'avitolog_4_more'
COMMAND_AVITOLOG_4_BACK = 'avitolog_4_back'

def avitolog_page_4():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<--- Назад', callback_data=COMMAND_AVITOLOG_4_BACK),
                InlineKeyboardButton(text='Вперёд --->', callback_data=COMMAND_AVITOLOG_4_MORE),
            ],
        ],
    )

COMMAND_AVITOLOG_5_BACK = 'avitolog_5_back'

def avitolog_page_5():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<--- Назад', callback_data=COMMAND_AVITOLOG_5_BACK),
            ],
        ],
    )


'''Инлайн кнопки для пагинации запросов по сммщикам'''


COMMAND_SMM_2 = 'smm_2'

def get_smm_page_two():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Вперёд --->', callback_data=COMMAND_SMM_2),
            ],
        ],
    )

COMMAND_SMM_2_MORE = 'smm_2_more'
COMMAND_SMM_2_BACK = 'smm_2_back'

def smm_page_2():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<--- Назад', callback_data=COMMAND_SMM_2_BACK),
                InlineKeyboardButton(text='Вперёд --->', callback_data=COMMAND_SMM_2_MORE),
            ],
        ],
    )

COMMAND_SMM_3_MORE = 'smm_3_more'
COMMAND_SMM_3_BACK = 'smm_3_back'

def smm_page_3():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<--- Назад', callback_data=COMMAND_SMM_3_BACK),
                InlineKeyboardButton(text='Вперёд --->', callback_data=COMMAND_SMM_3_MORE),
            ],
        ],
    )

COMMAND_SMM_4_MORE = 'smm_4_more'
COMMAND_SMM_4_BACK = 'smm_4_back'

def smm_page_4():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<--- Назад', callback_data=COMMAND_SMM_4_BACK),
                InlineKeyboardButton(text='Вперёд --->', callback_data=COMMAND_SMM_4_MORE),
            ],
        ],
    )

COMMAND_SMM_5_BACK = 'smm_5_back'

def smm_page_5():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<--- Назад', callback_data=COMMAND_SMM_5_BACK),
            ],
        ],
    )


'''Инлайн кнопки для пагинации запросов по чат-ботам'''


COMMAND_CHAT_BOTY_2 = 'chat_bots_2'

def get_chat_bots_page_two():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Вперёд --->', callback_data=COMMAND_CHAT_BOTY_2),
            ],
        ],
    )

COMMAND_CHAT_BOTY_2_MORE = 'chat_bots_2_more'
COMMAND_CHAT_BOTY_2_BACK = 'chat_bots_2_back'

def chat_bots_page_2():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<--- Назад', callback_data=COMMAND_CHAT_BOTY_2_BACK),
                InlineKeyboardButton(text='Вперёд --->', callback_data=COMMAND_CHAT_BOTY_2_MORE),
            ],
        ],
    )

COMMAND_CHAT_BOTY_3_MORE = 'chat_bots_3_more'
COMMAND_CHAT_BOTY_3_BACK = 'chat_bots_3_back'

def chat_bots_page_3():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<--- Назад', callback_data=COMMAND_CHAT_BOTY_3_BACK),
                InlineKeyboardButton(text='Вперёд --->', callback_data=COMMAND_CHAT_BOTY_3_MORE),
            ],
        ],
    )

COMMAND_CHAT_BOTY_4_MORE = 'chat_bots_4_more'
COMMAND_CHAT_BOTY_4_BACK = 'chat_bots_4_back'

def chat_bots_page_4():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<--- Назад', callback_data=COMMAND_CHAT_BOTY_4_BACK),
                InlineKeyboardButton(text='Вперёд --->', callback_data=COMMAND_CHAT_BOTY_4_MORE),
            ],
        ],
    )

COMMAND_CHAT_BOTY_5_BACK = 'chat_bots_5_back'

def chat_bots_page_5():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<--- Назад', callback_data=COMMAND_CHAT_BOTY_5_BACK),
            ],
        ],
    )


'''Инлайн кнопки для пагинации запросов по контент-мейкерам'''


COMMAND_CONTENT_MAKER_2 = 'content_maker_2'

def get_content_maker_page_two():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Вперёд --->', callback_data=COMMAND_CONTENT_MAKER_2),
            ],
        ],
    )

COMMAND_CONTENT_MAKER_2_MORE = 'content_maker_2_more'
COMMAND_CONTENT_MAKER_2_BACK = 'content_maker_2_back'

def content_maker_page_2():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<--- Назад', callback_data=COMMAND_CONTENT_MAKER_2_BACK),
                InlineKeyboardButton(text='Вперёд --->', callback_data=COMMAND_CONTENT_MAKER_2_MORE),
            ],
        ],
    )

COMMAND_CONTENT_MAKER_3_MORE = 'content_maker_3_more'
COMMAND_CONTENT_MAKER_3_BACK = 'content_maker_3_back'

def content_maker_page_3():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<--- Назад', callback_data=COMMAND_CONTENT_MAKER_3_BACK),
                InlineKeyboardButton(text='Вперёд --->', callback_data=COMMAND_CONTENT_MAKER_3_MORE),
            ],
        ],
    )

COMMAND_CONTENT_MAKER_4_MORE = 'content_maker_4_more'
COMMAND_CONTENT_MAKER_4_BACK = 'content_maker_4_back'

def content_maker_page_4():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<--- Назад', callback_data=COMMAND_CONTENT_MAKER_4_BACK),
                InlineKeyboardButton(text='Вперёд --->', callback_data=COMMAND_CONTENT_MAKER_4_MORE),
            ],
        ],
    )

COMMAND_CONTENT_MAKER_5_BACK = 'content_maker_5_back'

def content_maker_page_5():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<--- Назад', callback_data=COMMAND_CONTENT_MAKER_5_BACK),
            ],
        ],
    )


'''Инлайн кнопки для пагинации запросов по маркетологам'''


COMMAND_MARKETOLOG_2 = 'marketolog_2'

def get_marketolog_page_two():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Вперёд --->', callback_data=COMMAND_MARKETOLOG_2),
            ],
        ],
    )

COMMAND_MARKETOLOG_2_MORE = 'marketolog_2_more'
COMMAND_MARKETOLOG_2_BACK = 'marketolog_2_back'

def marketolog_page_2():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<--- Назад', callback_data=COMMAND_MARKETOLOG_2_BACK),
                InlineKeyboardButton(text='Вперёд --->', callback_data=COMMAND_MARKETOLOG_2_MORE),
            ],
        ],
    )

COMMAND_MARKETOLOG_3_MORE = 'marketolog_3_more'
COMMAND_MARKETOLOG_3_BACK = 'marketolog_3_back'

def marketolog_page_3():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<--- Назад', callback_data=COMMAND_MARKETOLOG_3_BACK),
                InlineKeyboardButton(text='Вперёд --->', callback_data=COMMAND_MARKETOLOG_3_MORE),
            ],
        ],
    )

COMMAND_MARKETOLOG_4_MORE = 'marketolog_4_more'
COMMAND_MARKETOLOG_4_BACK = 'marketolog_4_back'

def marketolog_page_4():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<--- Назад', callback_data=COMMAND_MARKETOLOG_4_BACK),
                InlineKeyboardButton(text='Вперёд --->', callback_data=COMMAND_MARKETOLOG_4_MORE),
            ],
        ],
    )

COMMAND_MARKETOLOG_5_BACK = 'marketolog_5_back'

def marketolog_page_5():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<--- Назад', callback_data=COMMAND_MARKETOLOG_5_BACK),
            ],
        ],
    )


'''Инлайн кнопки для пагинации запросов по продюсерам'''


COMMAND_PRODUCER_2 = 'producer_2'

def get_producer_page_two():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Вперёд --->', callback_data=COMMAND_PRODUCER_2),
            ],
        ],
    )

COMMAND_PRODUCER_2_MORE = 'producer_2_more'
COMMAND_PRODUCER_2_BACK = 'producer_2_back'

def producer_page_2():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<--- Назад', callback_data=COMMAND_PRODUCER_2_BACK),
                InlineKeyboardButton(text='Вперёд --->', callback_data=COMMAND_PRODUCER_2_MORE),
            ],
        ],
    )

COMMAND_PRODUCER_3_MORE = 'producer_3_more'
COMMAND_PRODUCER_3_BACK = 'producer_3_back'

def producer_page_3():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<--- Назад', callback_data=COMMAND_PRODUCER_3_BACK),
                InlineKeyboardButton(text='Вперёд --->', callback_data=COMMAND_PRODUCER_3_MORE),
            ],
        ],
    )

COMMAND_PRODUCER_4_MORE = 'producer_4_more'
COMMAND_PRODUCER_4_BACK = 'producer_4_back'

def producer_page_4():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<--- Назад', callback_data=COMMAND_PRODUCER_4_BACK),
                InlineKeyboardButton(text='Вперёд --->', callback_data=COMMAND_PRODUCER_4_MORE),
            ],
        ],
    )

COMMAND_PRODUCER_5_BACK = 'producer_5_back'

def producer_page_5():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<--- Назад', callback_data=COMMAND_PRODUCER_5_BACK),
            ],
        ],
    )


'''Инлайн кнопки для пагинации запросов по менеджерам блогеров'''


COMMAND_BLOGGER_MANAGER_2 = 'blogger_manager_2'

def get_blogger_manager_page_two():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Вперёд --->', callback_data=COMMAND_BLOGGER_MANAGER_2),
            ],
        ],
    )

COMMAND_BLOGGER_MANAGER_2_MORE = 'blogger_manager_2_more'
COMMAND_BLOGGER_MANAGER_2_BACK = 'blogger_manager_2_back'

def blogger_manager_page_2():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<--- Назад', callback_data=COMMAND_BLOGGER_MANAGER_2_BACK),
                InlineKeyboardButton(text='Вперёд --->', callback_data=COMMAND_BLOGGER_MANAGER_2_MORE),
            ],
        ],
    )

COMMAND_BLOGGER_MANAGER_3_MORE = 'blogger_manager_3_more'
COMMAND_BLOGGER_MANAGER_3_BACK = 'blogger_manager_3_back'

def blogger_manager_page_3():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<--- Назад', callback_data=COMMAND_BLOGGER_MANAGER_3_BACK),
                InlineKeyboardButton(text='Вперёд --->', callback_data=COMMAND_BLOGGER_MANAGER_3_MORE),
            ],
        ],
    )

COMMAND_BLOGGER_MANAGER_4_MORE = 'blogger_manager_4_more'
COMMAND_BLOGGER_MANAGER_4_BACK = 'blogger_manager_4_back'

def blogger_manager_page_4():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<--- Назад', callback_data=COMMAND_BLOGGER_MANAGER_4_BACK),
                InlineKeyboardButton(text='Вперёд --->', callback_data=COMMAND_BLOGGER_MANAGER_4_MORE),
            ],
        ],
    )

COMMAND_BLOGGER_MANAGER_5_BACK = 'blogger_manager_5_back'

def blogger_manager_page_5():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<--- Назад', callback_data=COMMAND_BLOGGER_MANAGER_5_BACK),
            ],
        ],
    )

COMMAND_FEEDBACK = 'feedback'
COMMAND_SEND_TO_CHANNEL = 'send_to_channel'

def manager_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Ответить на отзыв', callback_data=COMMAND_FEEDBACK),
            ],
            [
                InlineKeyboardButton(text='Отправить в канал', callback_data=COMMAND_SEND_TO_CHANNEL),
            ],
        ],
    )

def callback_handler(update: Update, context: CallbackContext):
    chat_id = update.effective_message.chat_id
    user = update.effective_user
    callback_data = update.callback_query.data
    current_text = update.effective_message.text

    if callback_data == COMMAND_LIST:
        messages = list_messages(user_id=user.id, limit=5)
        text = '\n\n'.join([f'О ком отзыв: {message_worker} \nИз какой сферы человек:{message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_worker, message_activity, message_review, message_link in messages])
        update.effective_message.reply_text(
            text=text,
            reply_markup=main_button
        )

    elif callback_data == COMMAND_NAME:
        context.bot.send_message(
            chat_id=chat_id,
            text="Вы можете найти отзывы по имени нажав на 'Найти по имени', либо посмотреть список всех нажав 'Посмотреть все имена'",
            reply_markup=ReplyKeyboardMarkup([['Найти по имени'], ['Посмотреть все имена']], resize_keyboard=True),
        )


    elif callback_data == COMMAND_ACTIVITY:
        update.callback_query.edit_message_text(
            text="Выберите профессию, по которой хотите найти отзывы",
            reply_markup=get_activities_page_one(),
        )

######################   ДИЗАЙН   ######################


    elif callback_data == COMMAND_DESIGN:
        messages = list_of_activities(activities='Дизайн', limit=5, offset = 0)
        if not messages:
            text = 'Про дизайнеров ещё не оставляли отзывов'
            update.effective_message.reply_text(
                text = text,
            )
        else:
            update.effective_message.reply_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=get_designers_page_two(),
            )

    elif callback_data == COMMAND_DESIGN_2:
        messages = list_of_activities(activities='Дизайн', limit=5, offset = 5)
        if not messages:
            text = 'Это все отзывы о дизайнерах'
            update.effective_message.reply_text(
                text=text,
        )
        else:
            update.callback_query.edit_message_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=designers_page_2(),
            )

    elif callback_data == COMMAND_DESIGN_2_BACK:
        messages = list_of_activities(activities='Дизайн', limit=5)
        update.callback_query.edit_message_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
            reply_markup=get_designers_page_two(),
        )

    elif callback_data == COMMAND_DESIGN_2_MORE:
        messages = list_of_activities(activities='Дизайн', limit=5, offset = 10)
        if not messages:
            text = 'Это все отзывы о дизайнерах'
            update.effective_message.reply_text(
                text=text,
        )
        else:
            update.callback_query.edit_message_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=designers_page_3(),
            )

    elif callback_data == COMMAND_DESIGN_3_BACK:
        messages = list_of_activities(activities='Дизайн', limit=5, offset = 5)
        update.callback_query.edit_message_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
            reply_markup=designers_page_2(),
        )

    elif callback_data == COMMAND_DESIGN_3_MORE:
        messages = list_of_activities(activities='Дизайн', limit=5, offset = 15)
        if not messages:
            text = 'Это все отзывы о дизайнерах'
            update.effective_message.reply_text(
                text=text,
        )
        else:
            update.callback_query.edit_message_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=designers_page_4(),
            )

    elif callback_data == COMMAND_DESIGN_4_BACK:
        messages = list_of_activities(activities='Дизайн', limit=5, offset = 10)
        update.callback_query.edit_message_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
            reply_markup=designers_page_3(),
        )

    elif callback_data == COMMAND_DESIGN_4_MORE:
        messages = list_of_activities(activities='Дизайн', limit=5, offset = 20)
        if not messages:
            text = 'Это все отзывы о дизайнерах'
            update.effective_message.reply_text(
                text=text,
        )
        else:
            update.callback_query.edit_message_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=designers_page_5(),
            )

    elif callback_data == COMMAND_DESIGN_5_BACK:
        messages = list_of_activities(activities='Дизайн', limit=5, offset = 15)
        update.callback_query.edit_message_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
            reply_markup=designers_page_3(),
        )


######################   ТАРГЕТ   ######################

    elif callback_data == COMMAND_TARGET:
        messages = list_of_activities(activities='Таргет', limit=5, offset = 0)
        if not messages:
            text = 'Про таргетологов ещё не оставляли отзывов'
            update.effective_message.reply_text(
                text = text,
            )
        else:
            update.effective_message.reply_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=get_target_page_two(),
            )

        update.effective_message.reply_text(
            text=text,
            reply_markup=get_target_page_two(),
        )
        
    elif callback_data == COMMAND_TARGET_2:
        messages = list_of_activities(activities='Таргет', limit=5, offset = 5)
        if not messages:
            text = 'Это все отзывы о таргетологах'
            update.effective_message.reply_text(
                text=text,
        )
        else:
            update.callback_query.edit_message_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=target_page_2(),
            )

    elif callback_data == COMMAND_TARGET_2_BACK:
        messages = list_of_activities(activities='Таргет', limit=5)
        update.callback_query.edit_message_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
            reply_markup=get_target_page_two(),
        )

    elif callback_data == COMMAND_TARGET_2_MORE:
        messages = list_of_activities(activities='Таргет', limit=5, offset = 10)
        if not messages:
            text = 'Это все отзывы о таргетологах'
            update.effective_message.reply_text(
                text=text,
        )
        else:
            update.callback_query.edit_message_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=target_page_3(),
            )

    elif callback_data == COMMAND_TARGET_3_BACK:
        messages = list_of_activities(activities='Таргет', limit=5, offset = 5)
        update.callback_query.edit_message_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
            reply_markup=target_page_2(),
        )

    elif callback_data == COMMAND_TARGET_3_MORE:
        messages = list_of_activities(activities='Таргет', limit=5, offset = 15)
        if not messages:
            text = 'Это все отзывы о таргетологах'
            update.effective_message.reply_text(
                text=text,
        )
        else:
            update.callback_query.edit_message_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=target_page_4(),
            )

    elif callback_data == COMMAND_TARGET_4_BACK:
        messages = list_of_activities(activities='Таргет', limit=5, offset = 10)
        update.callback_query.edit_message_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
            reply_markup=target_page_3(),
        )

    elif callback_data == COMMAND_TARGET_4_MORE:
        messages = list_of_activities(activities='Таргет', limit=5, offset = 20)
        if not messages:
            text = 'Это все отзывы о таргетологах'
            update.effective_message.reply_text(
                text=text,
        )
        else:
            update.callback_query.edit_message_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=target_page_5(),
            )

    elif callback_data == COMMAND_TARGET_5_BACK:
        messages = list_of_activities(activities='Таргет', limit=5, offset = 15)
        update.callback_query.edit_message_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
            reply_markup=target_page_3(),
        )


######################   МЕНЕДЖЕР   ######################


    elif callback_data == COMMAND_MANAGER:
        messages = list_of_activities(activities='Менеджмент', limit=5, offset = 0)
        if not messages:
            text = 'Про менеджеров ещё не оставляли отзывов'
            update.effective_message.reply_text(
                text = text,
            )
        else:
            update.effective_message.reply_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=get_manager_page_two(),
            )
        
    elif callback_data == COMMAND_MANAGER_2:
        messages = list_of_activities(activities='Менеджмент', limit=5, offset = 5)
        if not messages:
            text = 'Это все отзывы о менеджерах'
            update.effective_message.reply_text(
                text=text,
        )
        else:
            update.callback_query.edit_message_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=manager_page_2(),
            )

    elif callback_data == COMMAND_MANAGER_2_BACK:
        messages = list_of_activities(activities='Менеджмент', limit=5)
        update.callback_query.edit_message_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
            reply_markup=get_manager_page_two(),
        )

    elif callback_data == COMMAND_MANAGER_2_MORE:
        messages = list_of_activities(activities='Менеджмент', limit=5, offset = 10)
        if not messages:
            text = 'Это все отзывы о менеджерах'
            update.effective_message.reply_text(
                text=text,
        )
        else:
            update.callback_query.edit_message_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=manager_page_3(),
            )

    elif callback_data == COMMAND_MANAGER_3_BACK:
        messages = list_of_activities(activities='Менеджмент', limit=5, offset = 5)
        update.callback_query.edit_message_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
            reply_markup=manager_page_2(),
        )

    elif callback_data == COMMAND_MANAGER_3_MORE:
        messages = list_of_activities(activities='Менеджмент', limit=5, offset = 15)
        if not messages:
            text = 'Это все отзывы о менеджерах'
            update.effective_message.reply_text(
                text=text,
        )
        else:
            update.callback_query.edit_message_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=manager_page_4(),
            )

    elif callback_data == COMMAND_MANAGER_4_BACK:
        messages = list_of_activities(activities='Менеджмент', limit=5, offset = 10)
        update.callback_query.edit_message_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
            reply_markup=manager_page_3(),
        )

    elif callback_data == COMMAND_MANAGER_4_MORE:
        messages = list_of_activities(activities='Менеджмент', limit=5, offset = 20)
        if not messages:
            text = 'Это все отзывы о менеджерах'
            update.effective_message.reply_text(
                text=text,
        )
        else:
            update.callback_query.edit_message_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=manager_page_5(),
            )

    elif callback_data == COMMAND_MANAGER_5_BACK:
        messages = list_of_activities(activities='Менеджмент', limit=5, offset = 15)
        update.callback_query.edit_message_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
            reply_markup=manager_page_3(),
        )


######################   КОНТЕНТ-МЕНЕДЖЕР   ######################


    elif callback_data == COMMAND_CONTENT_MANAGER:
        messages = list_of_activities(activities='Контент-менеджер', limit=5, offset = 0)
        if not messages:
            text = 'Про контент-менеджеров ещё не оставляли отзывов'
            update.effective_message.reply_text(
                text = text,
            )
        else:
            update.effective_message.reply_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=get_content_manager_page_two(),
            )
        
    elif callback_data == COMMAND_CONTENT_MANAGER_2:
        messages = list_of_activities(activities='Контент-менеджер', limit=5, offset = 5)
        if not messages:
            text = 'Это все отзывы о контент-менеджерах'
            update.effective_message.reply_text(
                text=text,
        )
        else:
            update.callback_query.edit_message_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=content_manager_page_2(),
            )

    elif callback_data == COMMAND_CONTENT_MANAGER_2_BACK:
        messages = list_of_activities(activities='Контент-менеджер', limit=5)
        update.callback_query.edit_message_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
            reply_markup=get_content_manager_page_two(),
        )

    elif callback_data == COMMAND_CONTENT_MANAGER_2_MORE:
        messages = list_of_activities(activities='Контент-менеджер', limit=5, offset = 10)
        if not messages:
            text = 'Это все отзывы о контент-менеджерах'
            update.effective_message.reply_text(
                text=text,
        )
        else:
            update.callback_query.edit_message_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=content_manager_page_3(),
            )

    elif callback_data == COMMAND_CONTENT_MANAGER_3_BACK:
        messages = list_of_activities(activities='Контент-менеджер', limit=5, offset = 5)
        update.callback_query.edit_message_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
            reply_markup=content_manager_page_2(),
        )

    elif callback_data == COMMAND_CONTENT_MANAGER_3_MORE:
        messages = list_of_activities(activities='Контент-менеджер', limit=5, offset = 15)
        if not messages:
            text = 'Это все отзывы о контент-менеджерах'
            update.effective_message.reply_text(
                text=text,
        )
        else:
            update.callback_query.edit_message_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=content_manager_page_4(),
            )

    elif callback_data == COMMAND_CONTENT_MANAGER_4_BACK:
        messages = list_of_activities(activities='Контент-менеджер', limit=5, offset = 10)
        update.callback_query.edit_message_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
            reply_markup=content_manager_page_3(),
        )

    elif callback_data == COMMAND_CONTENT_MANAGER_4_MORE:
        messages = list_of_activities(activities='Контент-менеджер', limit=5, offset = 20)
        if not messages:
            text = 'Это все отзывы о контент-менеджерах'
            update.effective_message.reply_text(
                text=text,
        )
        else:
            update.callback_query.edit_message_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=content_manager_page_5(),
            )

    elif callback_data == COMMAND_CONTENT_MANAGER_5_BACK:
        messages = list_of_activities(activities='Контент-менеджер', limit=5, offset = 15)
        update.callback_query.edit_message_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
            reply_markup=content_manager_page_3(),
        )


######################   ВИДЕОГРАФ   ######################


    elif callback_data == COMMAND_VIDEOGRAPH:
        messages = list_of_activities(activities='Видеограф', limit=5, offset = 0)
        if not messages:
            text = 'Про видеографов ещё не оставляли отзывов'
            update.effective_message.reply_text(
                text = text,
            )
        else:
            update.effective_message.reply_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=get_videograph_page_two(),
            )
        
    elif callback_data == COMMAND_VIDEOGRAPH_2:
        messages = list_of_activities(activities='Видеограф', limit=5, offset = 5)
        if not messages:
            text = 'Это все отзывы о видеографах'
            update.effective_message.reply_text(
                text=text,
        )
        else:
            update.callback_query.edit_message_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=videograph_page_2(),
            )

    elif callback_data == COMMAND_VIDEOGRAPH_2_BACK:
        messages = list_of_activities(activities='Видеограф', limit=5)
        update.callback_query.edit_message_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
            reply_markup=get_videograph_page_two(),
        )

    elif callback_data == COMMAND_VIDEOGRAPH_2_MORE:
        messages = list_of_activities(activities='Видеограф', limit=5, offset = 10)
        if not messages:
            text = 'Это все отзывы о видеографах'
            update.effective_message.reply_text(
                text=text,
        )
        else:
            update.callback_query.edit_message_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=videograph_page_3(),
            )

    elif callback_data == COMMAND_VIDEOGRAPH_3_BACK:
        messages = list_of_activities(activities='Видеограф', limit=5, offset = 5)
        update.callback_query.edit_message_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
            reply_markup=videograph_page_2(),
        )

    elif callback_data == COMMAND_VIDEOGRAPH_3_MORE:
        messages = list_of_activities(activities='Видеограф', limit=5, offset = 15)
        if not messages:
            text = 'Это все отзывы о видеографах'
            update.effective_message.reply_text(
                text=text,
        )
        else:
            update.callback_query.edit_message_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=videograph_page_4(),
            )

    elif callback_data == COMMAND_VIDEOGRAPH_4_BACK:
        messages = list_of_activities(activities='Видеограф', limit=5, offset = 10)
        update.callback_query.edit_message_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
            reply_markup=videograph_page_3(),
        )

    elif callback_data == COMMAND_VIDEOGRAPH_4_MORE:
        messages = list_of_activities(activities='Видеограф', limit=5, offset = 20)
        if not messages:
            text = 'Это все отзывы о видеографах'
            update.effective_message.reply_text(
                text=text,
        )
        else:
            update.callback_query.edit_message_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=videograph_page_5(),
            )

    elif callback_data == COMMAND_VIDEOGRAPH_5_BACK:
        messages = list_of_activities(activities='Видеограф', limit=5, offset = 15)
        update.callback_query.edit_message_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
            reply_markup=videograph_page_3(),
        )


######################   ФОТОГРАФ   ######################


    elif callback_data == COMMAND_PHOTOGRAPHER:
        messages = list_of_activities(activities='Фотограф', limit=5, offset = 0)
        if not messages:
            text = 'Про фотографов ещё не оставляли отзывов'
            update.effective_message.reply_text(
                text = text,
            )
        else:
            update.effective_message.reply_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=get_photographer_page_two(),
            )
        
    elif callback_data == COMMAND_PHOTOGRAPHER_2:
        messages = list_of_activities(activities='Фотограф', limit=5, offset = 5)
        if not messages:
            text = 'Это все отзывы о фотографах'
            update.effective_message.reply_text(
                text=text,
        )
        else:
            update.callback_query.edit_message_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=photographer_page_2(),
            )

    elif callback_data == COMMAND_PHOTOGRAPHER_2_BACK:
        messages = list_of_activities(activities='Фотограф', limit=5)
        update.callback_query.edit_message_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
            reply_markup=get_photographer_page_two(),
        )

    elif callback_data == COMMAND_PHOTOGRAPHER_2_MORE:
        messages = list_of_activities(activities='Фотограф', limit=5, offset = 10)
        if not messages:
            text = 'Это все отзывы о фотографах'
            update.effective_message.reply_text(
                text=text,
        )
        else:
            update.callback_query.edit_message_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=photographer_page_3(),
            )

    elif callback_data == COMMAND_PHOTOGRAPHER_3_BACK:
        messages = list_of_activities(activities='Фотограф', limit=5, offset = 5)
        update.callback_query.edit_message_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
            reply_markup=photographer_page_2(),
        )

    elif callback_data == COMMAND_PHOTOGRAPHER_3_MORE:
        messages = list_of_activities(activities='Фотограф', limit=5, offset = 15)
        if not messages:
            text = 'Это все отзывы о фотографах'
            update.effective_message.reply_text(
                text=text,
        )
        else:
            update.callback_query.edit_message_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=photographer_page_4(),
            )

    elif callback_data == COMMAND_PHOTOGRAPHER_4_BACK:
        messages = list_of_activities(activities='Фотограф', limit=5, offset = 10)
        update.callback_query.edit_message_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
            reply_markup=photographer_page_3(),
        )

    elif callback_data == COMMAND_PHOTOGRAPHER_4_MORE:
        messages = list_of_activities(activities='Фотограф', limit=5, offset = 20)
        if not messages:
            text = 'Это все отзывы о фотографах'
            update.effective_message.reply_text(
                text=text,
        )
        else:
            update.callback_query.edit_message_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=photographer_page_5(),
            )

    elif callback_data == COMMAND_PHOTOGRAPHER_5_BACK:
        messages = list_of_activities(activities='Фотограф', limit=5, offset = 15)
        update.callback_query.edit_message_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
            reply_markup=photographer_page_3(),
        )



######################   КОПИРАЙТЕР   ######################


    elif callback_data == COMMAND_COPYWRITER:
        messages = list_of_activities(activities='Копирайтер', limit=5, offset = 0)
        if not messages:
            text = 'Про копирайтеров ещё не оставляли отзывов'
            update.effective_message.reply_text(
                text = text,
            )
        else:
            update.effective_message.reply_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=get_copywriter_page_two(),
            )
        
    elif callback_data == COMMAND_COPYWRITER_2:
        messages = list_of_activities(activities='Копирайтер', limit=5, offset = 5)
        if not messages:
            text = 'Это все отзывы о копирайтерах'
            update.effective_message.reply_text(
                text=text,
        )
        else:
            update.callback_query.edit_message_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=copywriter_page_2(),
            )

    elif callback_data == COMMAND_COPYWRITER_2_BACK:
        messages = list_of_activities(activities='Копирайтер', limit=5)
        update.callback_query.edit_message_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
            reply_markup=get_copywriter_page_two(),
        )

    elif callback_data == COMMAND_COPYWRITER_2_MORE:
        messages = list_of_activities(activities='Копирайтер', limit=5, offset = 10)
        if not messages:
            text = 'Это все отзывы о копирайтерах'
            update.effective_message.reply_text(
                text=text,
        )
        else:
            update.callback_query.edit_message_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=copywriter_page_3(),
            )

    elif callback_data == COMMAND_COPYWRITER_3_BACK:
        messages = list_of_activities(activities='Копирайтер', limit=5, offset = 5)
        update.callback_query.edit_message_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
            reply_markup=copywriter_page_2(),
        )

    elif callback_data == COMMAND_COPYWRITER_3_MORE:
        messages = list_of_activities(activities='Копирайтер', limit=5, offset = 15)
        if not messages:
            text = 'Это все отзывы о копирайтерах'
            update.effective_message.reply_text(
                text=text,
        )
        else:
            update.callback_query.edit_message_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=copywriter_page_4(),
            )

    elif callback_data == COMMAND_COPYWRITER_4_BACK:
        messages = list_of_activities(activities='Копирайтер', limit=5, offset = 10)
        update.callback_query.edit_message_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
            reply_markup=copywriter_page_3(),
        )

    elif callback_data == COMMAND_COPYWRITER_4_MORE:
        messages = list_of_activities(activities='Копирайтер', limit=5, offset = 20)
        if not messages:
            text = 'Это все отзывы о копирайтерах'
            update.effective_message.reply_text(
                text=text,
        )
        else:
            update.callback_query.edit_message_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=copywriter_page_5(),
            )

    elif callback_data == COMMAND_COPYWRITER_5_BACK:
        messages = list_of_activities(activities='Копирайтер', limit=5, offset = 15)
        update.callback_query.edit_message_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
            reply_markup=copywriter_page_3(),
        )


######################   КОНТЕКСТОЛОГ   ######################


    elif callback_data == COMMAND_KONTEKSTOLOG:
        messages = list_of_activities(activities='Контекстная реклама', limit=5, offset = 0)
        if not messages:
            text = 'Про контекстологов ещё не оставляли отзывов'
            update.effective_message.reply_text(
                text = text,
            )
        else:
            update.effective_message.reply_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=get_kontekstolog_page_two(),
            )
        
    elif callback_data == COMMAND_KONTEKSTOLOG_2:
        messages = list_of_activities(activities='Контекстная реклама', limit=5, offset = 5)
        if not messages:
            text = 'Это все отзывы о контекстологах'
            update.effective_message.reply_text(
                text=text,
        )
        else:
            update.callback_query.edit_message_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=kontekstolog_page_2(),
            )

    elif callback_data == COMMAND_KONTEKSTOLOG_2_BACK:
        messages = list_of_activities(activities='Контекстная реклама', limit=5)
        update.callback_query.edit_message_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
            reply_markup=get_kontekstolog_page_two(),
        )

    elif callback_data == COMMAND_KONTEKSTOLOG_2_MORE:
        messages = list_of_activities(activities='Контекстная реклама', limit=5, offset = 10)
        if not messages:
            text = 'Это все отзывы о контекстологах'
            update.effective_message.reply_text(
                text=text,
        )
        else:
            update.callback_query.edit_message_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=kontekstolog_page_3(),
            )

    elif callback_data == COMMAND_KONTEKSTOLOG_3_BACK:
        messages = list_of_activities(activities='Контекстная реклама', limit=5, offset = 5)
        update.callback_query.edit_message_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
            reply_markup=kontekstolog_page_2(),
        )

    elif callback_data == COMMAND_KONTEKSTOLOG_3_MORE:
        messages = list_of_activities(activities='Контекстная реклама', limit=5, offset = 15)
        if not messages:
            text = 'Это все отзывы о контекстологах'
            update.effective_message.reply_text(
                text=text,
        )
        else:
            update.callback_query.edit_message_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=kontekstolog_page_4(),
            )

    elif callback_data == COMMAND_KONTEKSTOLOG_4_BACK:
        messages = list_of_activities(activities='Контекстная реклама', limit=5, offset = 10)
        update.callback_query.edit_message_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
            reply_markup=kontekstolog_page_3(),
        )

    elif callback_data == COMMAND_KONTEKSTOLOG_4_MORE:
        messages = list_of_activities(activities='Контекстная реклама', limit=5, offset = 20)
        if not messages:
            text = 'Это все отзывы о контекстологах'
            update.effective_message.reply_text(
                text=text,
        )
        else:
            update.callback_query.edit_message_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=kontekstolog_page_5(),
            )

    elif callback_data == COMMAND_KONTEKSTOLOG_5_BACK:
        messages = list_of_activities(activities='Контекстная реклама', limit=5, offset = 15)
        update.callback_query.edit_message_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
            reply_markup=kontekstolog_page_3(),
        )


######################   АВИТОЛОГ   ######################


    elif callback_data == COMMAND_AVITOLOG:
        messages = list_of_activities(activities='Авитолог', limit=5, offset = 0)
        if not messages:
            text = 'Про авитологов ещё не оставляли отзывов'
            update.effective_message.reply_text(
                text = text,
            )
        else:
            update.effective_message.reply_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=get_avitolog_page_two(),
            )
        
    elif callback_data == COMMAND_AVITOLOG_2:
        messages = list_of_activities(activities='Авитолог', limit=5, offset = 5)
        if not messages:
            text = 'Это все отзывы о авитологах'
            update.effective_message.reply_text(
                text=text,
        )
        else:
            update.callback_query.edit_message_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=avitolog_page_2(),
            )

    elif callback_data == COMMAND_AVITOLOG_2_BACK:
        messages = list_of_activities(activities='Авитолог', limit=5)
        update.callback_query.edit_message_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
            reply_markup=get_avitolog_page_two(),
        )

    elif callback_data == COMMAND_AVITOLOG_2_MORE:
        messages = list_of_activities(activities='Авитолог', limit=5, offset = 10)
        if not messages:
            text = 'Это все отзывы о авитологах'
            update.effective_message.reply_text(
                text=text,
        )
        else:
            update.callback_query.edit_message_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=avitolog_page_3(),
            )

    elif callback_data == COMMAND_AVITOLOG_3_BACK:
        messages = list_of_activities(activities='Авитолог', limit=5, offset = 5)
        update.callback_query.edit_message_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
            reply_markup=avitolog_page_2(),
        )

    elif callback_data == COMMAND_AVITOLOG_3_MORE:
        messages = list_of_activities(activities='Авитолог', limit=5, offset = 15)
        if not messages:
            text = 'Это все отзывы о авитологах'
            update.effective_message.reply_text(
                text=text,
        )
        else:
            update.callback_query.edit_message_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=avitolog_page_4(),
            )

    elif callback_data == COMMAND_AVITOLOG_4_BACK:
        messages = list_of_activities(activities='Авитолог', limit=5, offset = 10)
        update.callback_query.edit_message_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
            reply_markup=avitolog_page_3(),
        )

    elif callback_data == COMMAND_AVITOLOG_4_MORE:
        messages = list_of_activities(activities='Авитолог', limit=5, offset = 20)
        if not messages:
            text = 'Это все отзывы о авитологах'
            update.effective_message.reply_text(
                text=text,
        )
        else:
            update.callback_query.edit_message_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=avitolog_page_5(),
            )

    elif callback_data == COMMAND_AVITOLOG_5_BACK:
        messages = list_of_activities(activities='Авитолог', limit=5, offset = 15)
        update.callback_query.edit_message_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
            reply_markup=avitolog_page_3(),
        )


######################   СММЩИК   ######################


    elif callback_data == COMMAND_SMM:
        messages = list_of_activities(activities='SMM-щик', limit=5, offset = 0)
        if not messages:
            text = 'Про SMM-щиков ещё не оставляли отзывов'
            update.effective_message.reply_text(
                text = text,
            )
        else:
            update.effective_message.reply_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=get_smm_page_two(),
            )
        
    elif callback_data == COMMAND_SMM_2:
        messages = list_of_activities(activities='SMM-щик', limit=5, offset = 5)
        if not messages:
            text = 'Это все отзывы о SMM-щиках'
            update.effective_message.reply_text(
                text=text,
        )
        else:
            update.callback_query.edit_message_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=smm_page_2(),
            )

    elif callback_data == COMMAND_SMM_2_BACK:
        messages = list_of_activities(activities='SMM-щик', limit=5)
        update.callback_query.edit_message_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
            reply_markup=get_smm_page_two(),
        )

    elif callback_data == COMMAND_SMM_2_MORE:
        messages = list_of_activities(activities='SMM-щик', limit=5, offset = 10)
        if not messages:
            text = 'Это все отзывы о SMM-щиках'
            update.effective_message.reply_text(
                text=text,
        )
        else:
            update.callback_query.edit_message_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=smm_page_3(),
            )

    elif callback_data == COMMAND_SMM_3_BACK:
        messages = list_of_activities(activities='SMM-щик', limit=5, offset = 5)
        update.callback_query.edit_message_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
            reply_markup=smm_page_2(),
        )

    elif callback_data == COMMAND_SMM_3_MORE:
        messages = list_of_activities(activities='SMM-щик', limit=5, offset = 15)
        if not messages:
            text = 'Это все отзывы о SMM-щиках'
            update.effective_message.reply_text(
                text=text,
        )
        else:
            update.callback_query.edit_message_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=smm_page_4(),
            )

    elif callback_data == COMMAND_SMM_4_BACK:
        messages = list_of_activities(activities='SMM-щик', limit=5, offset = 10)
        update.callback_query.edit_message_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
            reply_markup=smm_page_3(),
        )

    elif callback_data == COMMAND_SMM_4_MORE:
        messages = list_of_activities(activities='SMM-щик', limit=5, offset = 20)
        if not messages:
            text = 'Это все отзывы о SMM-щиках'
            update.effective_message.reply_text(
                text=text,
        )
        else:
            update.callback_query.edit_message_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=smm_page_5(),
            )

    elif callback_data == COMMAND_SMM_5_BACK:
        messages = list_of_activities(activities='SMM-щик', limit=5, offset = 15)
        update.callback_query.edit_message_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
            reply_markup=smm_page_3(),
        )


######################   ЧАТ-БОТЫ   ######################


    elif callback_data == COMMAND_CHAT_BOTY:
        messages = list_of_activities(activities='Разработчик чат-ботов', limit=5, offset = 0)
        if not messages:
            text = 'Про разработчиков чат-ботов ещё не оставляли отзывов'
            update.effective_message.reply_text(
                text = text,
            )
        else:
            update.effective_message.reply_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=get_chat_bots_page_two(),
            )
        
    elif callback_data == COMMAND_CHAT_BOTY_2:
        messages = list_of_activities(activities='Разработчик чат-ботов', limit=5, offset = 5)
        if not messages:
            text = 'Это все отзывы о разработчиках ботов'
            update.effective_message.reply_text(
                text=text,
        )
        else:
            update.callback_query.edit_message_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=chat_bots_page_2(),
            )

    elif callback_data == COMMAND_CHAT_BOTY_2_BACK:
        messages = list_of_activities(activities='Разработчик чат-ботов', limit=5)
        update.callback_query.edit_message_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
            reply_markup=get_chat_bots_page_two(),
        )

    elif callback_data == COMMAND_CHAT_BOTY_2_MORE:
        messages = list_of_activities(activities='Разработчик чат-ботов', limit=5, offset = 10)
        if not messages:
            text = 'Это все отзывы о разработчиках ботов'
            update.effective_message.reply_text(
                text=text,
        )
        else:
            update.callback_query.edit_message_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=chat_bots_page_3(),
            )

    elif callback_data == COMMAND_CHAT_BOTY_3_BACK:
        messages = list_of_activities(activities='Разработчик чат-ботов', limit=5, offset = 5)
        update.callback_query.edit_message_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
            reply_markup=chat_bots_page_2(),
        )

    elif callback_data == COMMAND_CHAT_BOTY_3_MORE:
        messages = list_of_activities(activities='Разработчик чат-ботов', limit=5, offset = 15)
        if not messages:
            text = 'Это все отзывы о разработчиках ботов'
            update.effective_message.reply_text(
                text=text,
        )
        else:
            update.callback_query.edit_message_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=chat_bots_page_4(),
            )

    elif callback_data == COMMAND_CHAT_BOTY_4_BACK:
        messages = list_of_activities(activities='Разработчик чат-ботов', limit=5, offset = 10)
        update.callback_query.edit_message_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
            reply_markup=chat_bots_page_3(),
        )

    elif callback_data == COMMAND_CHAT_BOTY_4_MORE:
        messages = list_of_activities(activities='Разработчик чат-ботов', limit=5, offset = 20)
        if not messages:
            text = 'Это все отзывы о разработчиках ботов'
            update.effective_message.reply_text(
                text=text,
        )
        else:
            update.callback_query.edit_message_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=chat_bots_page_5(),
            )

    elif callback_data == COMMAND_CHAT_BOTY_5_BACK:
        messages = list_of_activities(activities='Разработчик чат-ботов', limit=5, offset = 15)
        update.callback_query.edit_message_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
            reply_markup=chat_bots_page_3(),
        )


######################   КОНТЕНТ-МЕЙКЕР   ######################


    elif callback_data == COMMAND_CONTENT_MAKER:
        messages = list_of_activities(activities='Контент-мейкер', limit=5, offset = 0)
        if not messages:
            text = 'Про контент-мейкеров ещё не оставляли отзывов'
            update.effective_message.reply_text(
                text = text,
            )
        else:
            update.effective_message.reply_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=get_content_maker_page_two(),
            )
        
    elif callback_data == COMMAND_CONTENT_MAKER_2:
        messages = list_of_activities(activities='Контент-мейкер', limit=5, offset = 5)
        if not messages:
            text = 'Это все отзывы о контент-мейкерах'
            update.effective_message.reply_text(
                text=text,
        )
        else:
            update.callback_query.edit_message_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=content_maker_page_2(),
            )

    elif callback_data == COMMAND_CONTENT_MAKER_2_BACK:
        messages = list_of_activities(activities='Контент-мейкер', limit=5)
        update.callback_query.edit_message_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
            reply_markup=get_content_maker_page_two(),
        )

    elif callback_data == COMMAND_CONTENT_MAKER_2_MORE:
        messages = list_of_activities(activities='Контент-мейкер', limit=5, offset = 10)
        if not messages:
            text = 'Это все отзывы о контент-мейкерах'
            update.effective_message.reply_text(
                text=text,
        )
        else:
            update.callback_query.edit_message_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=content_maker_page_3(),
            )

    elif callback_data == COMMAND_CONTENT_MAKER_3_BACK:
        messages = list_of_activities(activities='Контент-мейкер', limit=5, offset = 5)
        update.callback_query.edit_message_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
            reply_markup=content_maker_page_2(),
        )

    elif callback_data == COMMAND_CONTENT_MAKER_3_MORE:
        messages = list_of_activities(activities='Контент-мейкер', limit=5, offset = 15)
        if not messages:
            text = 'Это все отзывы о контент-мейкерах'
            update.effective_message.reply_text(
                text=text,
        )
        else:
            update.callback_query.edit_message_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=content_maker_page_4(),
            )

    elif callback_data == COMMAND_CONTENT_MAKER_4_BACK:
        messages = list_of_activities(activities='Контент-мейкер', limit=5, offset = 10)
        update.callback_query.edit_message_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
            reply_markup=content_maker_page_3(),
        )

    elif callback_data == COMMAND_CONTENT_MAKER_4_MORE:
        messages = list_of_activities(activities='Контент-мейкер', limit=5, offset = 20)
        if not messages:
            text = 'Это все отзывы о контент-мейкерах'
            update.effective_message.reply_text(
                text=text,
        )
        else:
            update.callback_query.edit_message_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=content_maker_page_5(),
            )

    elif callback_data == COMMAND_CONTENT_MAKER_5_BACK:
        messages = list_of_activities(activities='Контент-мейкер', limit=5, offset = 15)
        update.callback_query.edit_message_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
            reply_markup=content_maker_page_3(),
        )


######################   МАРКЕТОЛОГ   ######################


    elif callback_data == COMMAND_MARKETOLOG:
        messages = list_of_activities(activities='Маркетолог', limit=5, offset = 0)
        if not messages:
            text = 'Про маркетологов ещё не оставляли отзывов'
            update.effective_message.reply_text(
                text = text,
            )
        else:
            update.effective_message.reply_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=get_marketolog_page_two(),
            )
        
    elif callback_data == COMMAND_MARKETOLOG_2:
        messages = list_of_activities(activities='Маркетолог', limit=5, offset = 5)
        if not messages:
            text = 'Это все отзывы о маркетологах'
            update.effective_message.reply_text(
                text=text,
        )
        else:
            update.callback_query.edit_message_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=marketolog_page_2(),
            )

    elif callback_data == COMMAND_MARKETOLOG_2_BACK:
        messages = list_of_activities(activities='Маркетолог', limit=5)
        update.callback_query.edit_message_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
            reply_markup=get_marketolog_page_two(),
        )

    elif callback_data == COMMAND_MARKETOLOG_2_MORE:
        messages = list_of_activities(activities='Маркетолог', limit=5, offset = 10)
        if not messages:
            text = 'Это все отзывы о маркетологах'
            update.effective_message.reply_text(
                text=text,
        )
        else:
            update.callback_query.edit_message_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=marketolog_page_3(),
            )

    elif callback_data == COMMAND_MARKETOLOG_3_BACK:
        messages = list_of_activities(activities='Маркетолог', limit=5, offset = 5)
        update.callback_query.edit_message_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
            reply_markup=marketolog_page_2(),
        )

    elif callback_data == COMMAND_MARKETOLOG_3_MORE:
        messages = list_of_activities(activities='Маркетолог', limit=5, offset = 15)
        if not messages:
            text = 'Это все отзывы о маркетологах'
            update.effective_message.reply_text(
                text=text,
        )
        else:
            update.callback_query.edit_message_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=marketolog_page_4(),
            )

    elif callback_data == COMMAND_MARKETOLOG_4_BACK:
        messages = list_of_activities(activities='Маркетолог', limit=5, offset = 10)
        update.callback_query.edit_message_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
            reply_markup=marketolog_page_3(),
        )

    elif callback_data == COMMAND_MARKETOLOG_4_MORE:
        messages = list_of_activities(activities='Маркетолог', limit=5, offset = 20)
        if not messages:
            text = 'Это все отзывы о маркетологах'
            update.effective_message.reply_text(
                text=text,
        )
        else:
            update.callback_query.edit_message_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=marketolog_page_5(),
            )

    elif callback_data == COMMAND_MARKETOLOG_5_BACK:
        messages = list_of_activities(activities='Маркетолог', limit=5, offset = 15)
        update.callback_query.edit_message_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
            reply_markup=marketolog_page_3(),
        )


######################   ПРОДЮСЕР   ######################


    elif callback_data == COMMAND_PRODUCER:
        messages = list_of_activities(activities='Продюсер', limit=5, offset = 0)
        if not messages:
            text = 'Про продюсеров ещё не оставляли отзывов'
            update.effective_message.reply_text(
                text = text,
            )
        else:
            update.effective_message.reply_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=get_producer_page_two(),
            )
        
    elif callback_data == COMMAND_PRODUCER_2:
        messages = list_of_activities(activities='Продюсер', limit=5, offset = 5)
        if not messages:
            text = 'Это все отзывы о продюсерах'
            update.effective_message.reply_text(
                text=text,
        )
        else:
            update.callback_query.edit_message_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=producer_page_2(),
            )

    elif callback_data == COMMAND_PRODUCER_2_BACK:
        messages = list_of_activities(activities='Продюсер', limit=5)
        update.callback_query.edit_message_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
            reply_markup=get_producer_page_two(),
        )

    elif callback_data == COMMAND_PRODUCER_2_MORE:
        messages = list_of_activities(activities='Продюсер', limit=5, offset = 10)
        if not messages:
            text = 'Это все отзывы о продюсерах'
            update.effective_message.reply_text(
                text=text,
        )
        else:
            update.callback_query.edit_message_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=producer_page_3(),
            )

    elif callback_data == COMMAND_PRODUCER_3_BACK:
        messages = list_of_activities(activities='Продюсер', limit=5, offset = 5)
        update.callback_query.edit_message_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
            reply_markup=producer_page_2(),
        )

    elif callback_data == COMMAND_PRODUCER_3_MORE:
        messages = list_of_activities(activities='Продюсер', limit=5, offset = 15)
        if not messages:
            text = 'Это все отзывы о продюсерах'
            update.effective_message.reply_text(
                text=text,
        )
        else:
            update.callback_query.edit_message_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=producer_page_4(),
            )

    elif callback_data == COMMAND_PRODUCER_4_BACK:
        messages = list_of_activities(activities='Продюсер', limit=5, offset = 10)
        update.callback_query.edit_message_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
            reply_markup=producer_page_3(),
        )

    elif callback_data == COMMAND_PRODUCER_4_MORE:
        messages = list_of_activities(activities='Продюсер', limit=5, offset = 20)
        if not messages:
            text = 'Это все отзывы о продюсерах'
            update.effective_message.reply_text(
                text=text,
        )
        else:
            update.callback_query.edit_message_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=producer_page_5(),
            )

    elif callback_data == COMMAND_PRODUCER_5_BACK:
        messages = list_of_activities(activities='Продюсер', limit=5, offset = 15)
        update.callback_query.edit_message_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
            reply_markup=producer_page_3(),
        )


######################   МЕНЕДЖЕР-БЛОГЕРОВ   ######################


    elif callback_data == COMMAND_BLOGGER_MANAGER:
        messages = list_of_activities(activities='Менеджер по блогерам', limit=5, offset = 0)
        if not messages:
            text = 'Про менеджеров по блогерам ещё не оставляли отзывов'
        else:
            update.effective_message.reply_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=get_blogger_manager_page_two(),
            )
        update.effective_message.reply_text(
            text=text,
        )
        
    elif callback_data == COMMAND_BLOGGER_MANAGER_2:
        messages = list_of_activities(activities='Менеджер по блогерам', limit=5, offset = 5)
        if not messages:
            text = 'Это все отзывы о менеджерах по блогерам'
            update.effective_message.reply_text(
                text=text,
        )
        else:
            update.callback_query.edit_message_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=blogger_manager_page_2(),
            )

    elif callback_data == COMMAND_BLOGGER_MANAGER_2_BACK:
        messages = list_of_activities(activities='Менеджер по блогерам', limit=5)
        update.callback_query.edit_message_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
            reply_markup=get_blogger_manager_page_two(),
        )

    elif callback_data == COMMAND_BLOGGER_MANAGER_2_MORE:
        messages = list_of_activities(activities='Менеджер по блогерам', limit=5, offset = 10)
        if not messages:
            text = 'Это все отзывы о менеджерах по блогерам'
            update.effective_message.reply_text(
                text=text,
        )
        else:
            update.callback_query.edit_message_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=blogger_manager_page_3(),
            )

    elif callback_data == COMMAND_BLOGGER_MANAGER_3_BACK:
        messages = list_of_activities(activities='Менеджер по блогерам', limit=5, offset = 5)
        update.callback_query.edit_message_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
            reply_markup=blogger_manager_page_2(),
        )

    elif callback_data == COMMAND_BLOGGER_MANAGER_3_MORE:
        messages = list_of_activities(activities='Менеджер по блогерам', limit=5, offset = 15)
        if not messages:
            text = 'Это все отзывы о менеджерах по блогерам'
            update.effective_message.reply_text(
                text=text,
        )
        else:
            update.callback_query.edit_message_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=blogger_manager_page_4(),
            )

    elif callback_data == COMMAND_BLOGGER_MANAGER_4_BACK:
        messages = list_of_activities(activities='Менеджер по блогерам', limit=5, offset = 10)
        update.callback_query.edit_message_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
            reply_markup=blogger_manager_page_3(),
        )

    elif callback_data == COMMAND_BLOGGER_MANAGER_4_MORE:
        messages = list_of_activities(activities='Менеджер по блогерам', limit=5, offset = 20)
        if not messages:
            text = 'Это все отзывы о менеджерах по блогерам'
            update.effective_message.reply_text(
                text=text,
        )
        else:
            update.callback_query.edit_message_text(
                text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
                reply_markup=blogger_manager_page_5(),
            )

    elif callback_data == COMMAND_BLOGGER_MANAGER_5_BACK:
        messages = list_of_activities(activities='Менеджер по блогерам', limit=5, offset = 15)
        update.callback_query.edit_message_text(
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
            reply_markup=blogger_manager_page_3(),
        )

    elif callback_data == COMMAND_MORE:
        update.callback_query.edit_message_text(
            text=current_text,
            reply_markup=get_activities_page_two(),
        )

    elif callback_data == COMMAND_BACK:
        update.callback_query.edit_message_text(
            text=current_text,
            reply_markup=get_activities_page_one(),
        )

    elif callback_data == COMMAND_FEEDBACK:
        context.bot.send_message(
            text=current_text,
            chat_id=user.id,
        )
        print(chat_id)