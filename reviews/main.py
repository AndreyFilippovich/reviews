import telegram
import logging
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler, CallbackQueryHandler)

from buttons import *

from db import init_db, add_message, list_of_workers

import os

from dotenv import load_dotenv

load_dotenv()
init_db()

secret_token = os.getenv('TOKEN')
secret_chat_id = os.getenv('CHAT_ID')
secret_feedback_chat_id = os.getenv('FEEDBACK_USER_ID')

reply_keyboard = [['Подтвердить', 'Заново']]
markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

bot = telegram.Bot(token=secret_token)

def start(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    button = ReplyKeyboardMarkup([['Оставить отзыв'], ['Найти отзыв'], ['Помощь']], resize_keyboard=True, one_time_keyboard=True)
    context.bot.send_message(
        chat_id=chat.id,
        text='Привет, {}. Я бот, который позволит тебе найти или же оставить отзыв о компаниях и даже людях!\n'
             'Давай расскажу тебе, что умею: \n'
             'При нажатии команды "Оставить отзыв", ты можешь оставить отзыв.\n'
             'При нажатии команды "Найти отзыв", ты можешь найти отзыв.\n'
             'Если возникнут вопросы, то ты всегда поможет команда "Помощь".\n'.format(name),
        reply_markup=button
    )

main_button = ReplyKeyboardMarkup([['Оставить отзыв'], ['Найти отзыв'], ['Помощь']], resize_keyboard=True)
choose_button=ReplyKeyboardMarkup([['Дизайн'], ['Таргет'], ['Менеджмент'], ['Контент-менеджер'], ['Видео-мейкер'], ['Фотограф'],
                                  ['Копирайтер'], ['Контекстная реклама'], ['Авитолог'], ['SMM-щик'], ['Разработчик чат-ботов'],
                                  ['Контент-мейкер'], ['Маркетолог'], ['Продюсер'], ['Менеджер по блогерам']], resize_keyboard=True, one_time_keyboard=True)

def help(update, context):
    chat = update.effective_chat
    context.bot.send_message(
        chat_id=chat.id,
        text='Давай расскажу тебе подробнее про каждую из команд: \n'
             'Нажмите на команду "Оставить отзыв" для написания отзыва. \n'
             'Бот будет задавать тебе вопросы по поводу компании, по итогам которой будет сформирован отзыв. \n'
             'Если что-то перепутали или не хотите отвечать, то после каждого вопроса есть команды /skip или же /cancel. \n'
             'В конце вам нужно будет проверить корректность заполнения отзыва. \n'
             'Отзыв будет отправлен модератору и если все пройдет удачно, то ваш отзыв будет опубликован в канале, \n'
             'а если будут ошибки, то модератор отправит вам его обратно с комментарием.',
        reply_markup=main_button
    )

def facts_to_str(user_data):
    facts = list() 
    for key, value in user_data.items():
        facts.append('{} - {}'.format(key, value))

    return "\n".join(facts).join(['\n', '\n'])

NAME, WORKER, ACTIVITY, REVIEW, PHOTO, LINK, CONFIRMATION = range(7)

def leave_review(update, context):
    update.message.reply_text(
        'Для начала необходимо узнать ваше имя.\n\n'
        'Если не хотите указывать имя, то нажмите на кнопку "Анонимно"\n\n'
        'Команда /cancel, чтобы прекратить написание отзыва.',
        reply_markup=ReplyKeyboardMarkup([['Анонимно']], resize_keyboard=True),
        )
    return NAME

def name(update, context):
    user = update.message.from_user
    user_data = context.user_data
    category = 'Имя'
    text = update.message.text
    user_data[category] = text
    logger.info("Собственное имя %s: %s", user.first_name, update.message.text)
    update.message.reply_text('Спасибо. Пойдем дальше! \n'
                              'Теперь введите имя человека о котором хотите оставить отзыв.\n\n'
                              'Команда /cancel, чтобы прекратить написание отзыва.',
                              reply_markup=ReplyKeyboardRemove(),
                              )
    return WORKER

def worker(update, context):
    user = update.message.from_user
    user_data = context.user_data
    category = 'О ком отзыв'
    text = update.message.text
    user_data[category] = text
    logger.info("Отзыв будет писаться о %s: %s", user.first_name, update.message.text)
    update.message.reply_text('Отлично! Теперь выберите из какой сферы данный человек.\n\n'
                              'Команда /cancel, чтобы прекратить написание отзыва.',
                              reply_markup=choose_button,
                              )
    return ACTIVITY

def activity(update, context):
    user = update.message.from_user
    user_data = context.user_data
    category = 'Сфера деятельности'
    text = update.message.text
    user_data[category] = text
    logger.info("Сфера деятельности %s: %s", user.first_name, update.message.text)
    update.message.reply_text('Отлично! Теперь напишите сам отзыв.\n\n'
                              'Команда /cancel, чтобы прекратить написание отзыва.',
                              reply_markup=ReplyKeyboardRemove(),
                              )
    return REVIEW

def review(update, context):
    user = update.message.from_user
    user_data = context.user_data
    category = 'Отзыв'
    text = update.message.text
    user_data[category] = text    
    logger.info("Отзыв %s: %s", user.first_name, update.message.text)
    update.message.reply_text('Супер! Осталось совсем немного! \n'
                              'В ответном сообщении вы можете прикрепить фото к отыву.\n\n'
                              'Если у вас нет фото, то нажмите на кнопку /skip.\n'
                              'Команда /cancel, чтобы прекратить написание отзыва.',
                              reply_markup=ReplyKeyboardRemove(),
                              )
    return PHOTO


def photo(update, context):
    user = update.message.from_user
    photo_file = update.message.photo[-1].get_file()
    photo_file.download(f'{user.first_name}_photo.jpg')
    logger.info("Фотография %s: %s", user.first_name, f'{user.first_name}_photo.jpg')
    update.message.reply_text('Замечательно! Остался последний пункт.'
                              'Укажите ссылку на компанию!\n\n'
                              'Команда /cancel, чтобы прекратить написание отзыва.',
                              reply_markup=ReplyKeyboardRemove(),)
    return LINK


def skip_photo(update, context):
    user = update.message.from_user
    logger.info("Пользователь %s не отправил фото.", user.first_name)
    update.message.reply_text('С фотографией было бы гораздо лучше, но заставлять не будем. \n'
                              'Остался последний пункт! \n'
                              'Укажите ссылку на компанию!\n\n'
                              'Команда /cancel, чтобы прекратить написание отзыва.',
                              reply_markup=ReplyKeyboardRemove(),
                              )
    return LINK

def link(update, context):
    user = update.message.from_user
    user_data = context.user_data
    category = 'Ссылка'
    text = update.message.text
    user_data[category] = text 
    logger.info("Ссылка %s: %s", user.first_name, update.message.text)
    update.message.reply_text('Спасибо вам за отзыв! Пожалуйста, проверьте информацию на корректность:'
                              '{}'.format(facts_to_str(user_data)), reply_markup=markup)

    return CONFIRMATION

def confirmation(update, context):
    chat_id = update.message.chat_id
    user_data = context.user_data
    user = update.message.from_user
    update.message.reply_text('Спасибо! Информация будет отправлена менеджеру на модерацию', reply_markup=main_button)
    bot.send_photo(chat_id=secret_feedback_chat_id, photo=open(f'{user.first_name}_photo.jpg', 'rb'), 
                   caption="Новый отзыв от пользователя {}".format(user.name) + ":\n {}".format(facts_to_str(user_data)),
                   parse_mode=telegram.ParseMode.HTML, reply_markup=manager_keyboard())

    add_message(
        user_id=user.id,
        name=user_data['Имя'],
        worker=user_data['О ком отзыв'],
        activity=user_data['Сфера деятельности'],
        review=user_data['Отзыв'],
        link=user_data['Ссылка']
    )

def cancel(update, _):
    user = update.message.from_user
    logger.info("Пользователь %s отменил разговор.", user.first_name)
    button = ReplyKeyboardMarkup([['Оставить отзыв'], ['Найти отзыв'], ['Помощь']], resize_keyboard=True)
    update.message.reply_text(
        'Мое дело предложить - Ваше отказаться \n'
        'Ждем вас снова!\n\n'
        'Если хотите написать отзыв то нажмите "Оставить отзыв" \n'
        'Если хотите найти отзыв то нажмите "Найти отзыв" \n'
        'Во всех остальных случаях поможет команда "Помощь"', 
        reply_markup=button
    )
    return ConversationHandler.END

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def find_review(update, context):
    update.message.reply_text(
        'Тестируем\n\n'
        'Если не хотите указывать имя, то нажмите на кнопку "Анонимно"\n\n'
        'Команда /cancel, чтобы прекратить написание отзыва.',
        reply_markup=get_keyboard()
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

# def get_all_workers(update, context):
#     messages = all_workers(worker='', limit=5)
#     update.message.reply_text(
#         text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages]),
#         reply_markup=get_keyboard()
#         )


def main():

    updater = Updater(token=secret_token)
#     updater.dispatcher.add_handler(MessageHandler(Filters.regex('^Посмотреть все имена$'), get_all_workers))

    updater.dispatcher.add_handler(CallbackQueryHandler(callback_handler))

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex('^Помощь$'), help))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex('^Найти отзыв$'), find_review))

    conv_handler = ConversationHandler(
        [MessageHandler(Filters.regex('^Оставить отзыв$'), leave_review)],

        states={
            NAME: [MessageHandler(Filters.text & ~Filters.command, name)],
            WORKER: [MessageHandler(Filters.text & ~Filters.command, worker)],
            ACTIVITY: [MessageHandler(Filters.text & ~Filters.command, activity)],
            REVIEW: [MessageHandler(Filters.text & ~Filters.command, review)],
            PHOTO: [MessageHandler(Filters.photo, photo), CommandHandler('skip', skip_photo)],
            LINK: [MessageHandler(Filters.text & ~Filters.command, link)],
            CONFIRMATION: [MessageHandler(Filters.regex('^Подтвердить$'),
                                      confirmation),
            MessageHandler(Filters.regex('^Заново$'), leave_review),
            MessageHandler(Filters.regex('^Оставить отзыв$'), leave_review)
                       ],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    updater.dispatcher.add_handler(conv_handler)

    conv_handler_2 = ConversationHandler(
        [MessageHandler(Filters.regex('^Найти по имени$'), ask_worker_name)],

        states = {
            WORKER_NAME: [MessageHandler(Filters.text & ~Filters.command, finish_worker_name)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    updater.dispatcher.add_handler(conv_handler_2)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
