import telegram

from main import logger

from buttons import markup, choose_button, main_button
from keyboards import manager_keyboard

from db import add_message
from config import secret_feedback_chat_id, bot

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup
from telegram.ext import ConversationHandler
from datetime import datetime

def present_time():
    today = datetime.utcnow()
    return today



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
    logger.info("Собственное имя %s: %s", user.first_name, text)
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
    logger.info("Отзыв будет писаться о %s: %s", user.first_name, text)
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
    logger.info("Сфера деятельности %s: %s", user.first_name, text)
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
    logger.info("Отзыв %s: %s", user.first_name, text)
    update.message.reply_text('Супер! Осталось совсем немного! \n'
                              'В ответном сообщении вы можете прикрепить фото к отыву.\n\n'
                              'Если у вас нет фото, то нажмите на кнопку /skip.\n'
                              'Команда /cancel, чтобы прекратить написание отзыва.',
                              reply_markup=ReplyKeyboardRemove(),
                              )
    return PHOTO


def photo(update, context):
    user = update.message.from_user
    user_data = context.user_data
    photo_file = update.message.photo[-1].get_file()
    photo_file.download(f'photos/{user.first_name}.{present_time()}_photo.jpg')
    category = 'Фото'
    user_data[category] = f'photos/{user.first_name}.{present_time()}_photo.jpg'
    logger.info("Фотография %s: %s", user.first_name, f'{user.first_name}_photo.jpg')
    update.message.reply_text('Замечательно! Остался последний пункт.'
                              'Укажите ссылку на компанию!\n\n'
                              'Команда /cancel, чтобы прекратить написание отзыва.',
                              reply_markup=ReplyKeyboardRemove(),)
    return LINK


def skip_photo(update, context):
    user = update.message.from_user
    user_data = context.user_data
    category = 'Фото'
    user_data[category] = 'no'
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
    logger.info("Ссылка %s: %s", user.first_name, text)
    bot.send_photo(chat_id=user.id, photo=open(f'photos/{user.first_name}.{present_time()}_photo.jpg', 'rb'),
                   caption='Спасибо вам за отзыв! Пожалуйста, проверьте информацию на корректность:\n\n'
                   '{}'.format(facts_to_str(user_data)), reply_markup=markup)

    return CONFIRMATION

def confirmation(update, context):
    user_data = context.user_data
    user = update.message.from_user
    update.message.reply_text('Спасибо! Информация будет отправлена менеджеру на модерацию', reply_markup=main_button)
    bot.send_photo(chat_id=secret_feedback_chat_id, photo=open(f'photos/{user.first_name}.{present_time()}_photo.jpg', 'rb'), 
                   caption="Новый отзыв от пользователя {}".format(user.name) + ":\n {}".format(facts_to_str(user_data)),
                   parse_mode=telegram.ParseMode.HTML, reply_markup=InlineKeyboardMarkup(manager_keyboard))
    
    print(user_data['Фото'])

    add_message(
        user_id=user.id,
        name=user_data['Имя'],
        worker=user_data['О ком отзыв'],
        activity=user_data['Сфера деятельности'],
        review=user_data['Отзыв'],
        photo=user_data['Фото'],
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
