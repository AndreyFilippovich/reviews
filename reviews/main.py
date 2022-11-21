import telegram
import logging
from telegram import Update
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove,
                      InlineKeyboardButton, InlineKeyboardMarkup)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler, CallbackQueryHandler)

from telegram.ext import CallbackContext

from db import (init_db, add_message, count_messages, list_messages,
                list_of_designers, list_of_target, list_of_menedger,
                list_of_content_menedger, list_of_videograph,
                list_of_photographer, list_of_copywriter,
                list_of_contekstolog, list_of_avitolog,
                list_of_smm, list_of_chat_bots,
                list_of_content_maker, list_of_marketolog,
                list_of_producer, list_of_blogger_manager)

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
    button = ReplyKeyboardMarkup([['Оставить отзыв'], ['Найти отзыв'], ['Помощь']], resize_keyboard=True)
    context.bot.send_message(
        chat_id=chat.id,
        text='Привет, {}. Я бот, который позволит тебе найти или же оставить отзыв о компаниях и даже людях!\n'
             'Давай расскажу тебе, что умею: \n'
             'При нажатии команды "Оставить отзыв", ты можешь оставить отзыв.\n'
             'При нажатии команды "Найти отзыв", ты можешь найти отзыв.\n'
             'Если возникнут вопросы, то ты всегда поможет команда "Помощь".\n'.format(name),
        reply_markup=button
    )

def help(update, context):
    chat = update.effective_chat
    button = ReplyKeyboardMarkup([['Оставить отзыв'], ['Найти отзыв'], ['Помощь']], resize_keyboard=True)
    context.bot.send_message(
        chat_id=chat.id,
        text='Давай расскажу тебе подробнее про каждую из команд: \n'
             'Нажмите на команду "Оставить отзыв" для написания отзыва. \n'
             'Бот будет задавать тебе вопросы по поводу компании, по итогам которой будет сформирован отзыв. \n'
             'Если что-то перепутали или не хотите отвечать, то после каждого вопроса есть команды /skip или же /cancel. \n'
             'В конце вам нужно будет проверить корректность заполнения отзыва. \n'
             'Отзыв будет отправлен модератору и если все пройдет удачно, то ваш отзыв будет опубликован в канале, \n'
             'а если будут ошибки, то модератор отправит вам его обратно с комментарием.',
        reply_markup=button
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
                              reply_markup=ReplyKeyboardMarkup([['Дизайн'], 
                                                                ['Таргет'], 
                                                                ['Менеджмент'],
                                                                ['Контент-менеджер'],
                                                                ['Видео-мейкер'],
                                                                ['Фотограф'],
                                                                ['Копирайтер']
                                                                ], resize_keyboard=True),
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
    user_data = context.user_data
    user = update.message.from_user
    update.message.reply_text('Спасибо! Информация будет отправлена менеджеру на модерацию', reply_markup=ReplyKeyboardRemove())
    bot.send_photo(chat_id=secret_feedback_chat_id, photo=open(f'{user.first_name}_photo.jpg', 'rb'), 
                   caption="Новый отзыв от пользователя {}".format(user.name) + ":\n {}".format(facts_to_str(user_data)),
                   parse_mode=telegram.ParseMode.HTML)

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

COMMAND_COUNT = 'count'
COMMAND_LIST = 'list'
COMMAND_ACTIVITY = 'choose'

def get_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Кол-во сообщений', callback_data=COMMAND_COUNT),
            ],
            [
                InlineKeyboardButton(text='Мои сообщения', callback_data=COMMAND_LIST),
            ],
            [
                InlineKeyboardButton(text='Найти по профессии', callback_data=COMMAND_ACTIVITY),
            ],
        ],
    )
COMMAND_DESIGN = 'designer'
COMMAND_TARGET = 'target'
COMMAND_MENEDGMENT = 'menedger'
COMMAND_CONTENT_MENEDGER = 'content_menedger'
COMMAND_VIDEOGRAPH = 'videograph'
COMMAND_PHOTOGRAPHER = 'photographer'
COMMAND_COPYWRITER = 'copywriter'
COMMAND_MORE = 'more'

COMMAND_KONTEKSTOLOG = 'kontekstolog'
COMMAND_AVITOLOG = 'avitolog'
COMMAND_SMM = 'SMM'
COMMAND_CHAT_BOTY ='chat-bots'
COMMAND_CONTENT_MAKER ='content maker'
COMMAND_MARKETOLOG = 'marketolog'
COMMAND_PRODUCER = 'producer'
COMMAND_BLOGGER_MANAGER = 'blogger manager'
COMMAND_BACK = 'back'

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
                InlineKeyboardButton(text='Менеджмент', callback_data=COMMAND_MENEDGMENT),
            ],
            [
                InlineKeyboardButton(text='Контент-менеджер', callback_data=COMMAND_CONTENT_MENEDGER),
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


def callback_handler(update: Update, context: CallbackContext):
    user = update.effective_user
    callback_data = update.callback_query.data
    current_text = update.effective_message.text

    if callback_data == COMMAND_COUNT:
        count = count_messages(user_id=user.id)
        text = f'У вас {count} сообщений!'
    elif callback_data == COMMAND_LIST:
        messages = list_messages(user_id=user.id, limit=5)
        text = '\n\n'.join([f'О ком отзыв: {message_worker} \nИз какой сферы человек:{message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_worker, message_activity, message_review, message_link in messages])
        update.effective_message.reply_text(
            text=text,
        )    
    elif callback_data == COMMAND_ACTIVITY:
        # Показать следующий экран клавиатуры
        # (оставить тот же текст, но указать другой массив кнопок)
        update.callback_query.edit_message_text(
            text="Выберите профессию, по которой хотите найти отзывы",
            reply_markup=get_activities_page_one(),
        )
    elif callback_data == COMMAND_DESIGN:
        messages = list_of_designers(activities='Дизайн')
        text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages])
        update.effective_message.reply_text(
            text=text,
        )

    elif callback_data == COMMAND_TARGET:
        messages = list_of_designers(activities='Таргет')
        text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages])
        update.effective_message.reply_text(
            text=text,
        )

    elif callback_data == COMMAND_MENEDGMENT:
        messages = list_of_designers(activities='Менеджмент')
        text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages])

        update.effective_message.reply_text(
            text=text,
        )

    elif callback_data == COMMAND_CONTENT_MENEDGER:
        try:
            messages = list_of_designers(activities='Контент-менеджер')
            text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages])
        except Exception as error:
            text = 'Ошибка'
        update.effective_message.reply_text(
            text=text,
        )

    elif callback_data == COMMAND_VIDEOGRAPH:
        messages = list_of_designers(activities='Видеограф')
        text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages])

        update.effective_message.reply_text(
            text=text,
        )

    elif callback_data == COMMAND_PHOTOGRAPHER:
        messages = list_of_designers(activities='Фотограф')
        text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages])

        update.effective_message.reply_text(
            text=text,
        )

    elif callback_data == COMMAND_COPYWRITER:
        messages = list_of_designers(activities='Копирайтер')
        text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages])

        update.effective_message.reply_text(
            text=text,
        )

    elif callback_data == COMMAND_KONTEKSTOLOG:
        messages = list_of_designers(activities='Контекстная реклама')
        text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages])

        update.effective_message.reply_text(
            text=text,
        )

    elif callback_data == COMMAND_AVITOLOG:
        messages = list_of_designers(activities='Авитолог')
        text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages])

        update.effective_message.reply_text(
            text=text,
        )

    elif callback_data == COMMAND_SMM:
        messages = list_of_designers(activities='SMM-щик')
        text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages])

        update.effective_message.reply_text(
            text=text,
        )

    elif callback_data == COMMAND_CHAT_BOTY:
        messages = list_of_designers(activities='Разработчик чат-ботов')
        text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages])

        update.effective_message.reply_text(
            text=text,
        )

    elif callback_data == COMMAND_CONTENT_MAKER:
        messages = list_of_designers(activities='Контент-мейкер')
        text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages])

        update.effective_message.reply_text(
            text=text,
        )

    elif callback_data == COMMAND_MARKETOLOG:
        messages = list_of_designers(activities='Маркетолог')
        text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages])

        update.effective_message.reply_text(
            text=text,
        )

    elif callback_data == COMMAND_PRODUCER:
        messages = list_of_designers(activities='Продюсер')
        text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages])

        update.effective_message.reply_text(
            text=text,
        )

    elif callback_data == COMMAND_BLOGGER_MANAGER:
        messages = list_of_designers(activities='Менеджер по блогерам')
        text = '\n\n'.join([f'Кто написал отзыв: {message_name} \nО ком отзыв: {message_worker} \nИз какой сферы человек: {message_activity} \nОтзыв: {message_review} \nСсылка: {message_link}' for message_name, message_worker, message_activity, message_review, message_link in messages])

        update.effective_message.reply_text(
            text=text,
        )

    elif callback_data == COMMAND_MORE:
        # Показать следующий экран клавиатуры
        # (оставить тот же текст, но указать другой массив кнопок)
        update.callback_query.edit_message_text(
            text=current_text,
            reply_markup=get_activities_page_two(),
        )

    elif callback_data == COMMAND_BACK:
        # Показать предыдущий экран клавиатуры
        # (оставить тот же текст, но указать другой массив кнопок)
        update.callback_query.edit_message_text(
            text=current_text,
            reply_markup=get_activities_page_one(),
        )


def find_review(update, context):
    update.message.reply_text(
        'Тестируем\n\n'
        'Если не хотите указывать имя, то нажмите на кнопку "Анонимно"\n\n'
        'Команда /cancel, чтобы прекратить написание отзыва.',
        reply_markup=get_keyboard(),
        )


def main():

    updater = Updater(token=secret_token)

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


    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()