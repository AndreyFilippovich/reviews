import telegram
import logging
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler, CallbackContext)

import os

from dotenv import load_dotenv

load_dotenv()

secret_token = os.getenv('TOKEN')
secret_chat_id = os.getenv('CHAT_ID')
secret_feedback_chat_id = os.getenv('FEEDBACK_USER_ID')

reply_keyboard = [['Confirm', 'Restart']]
markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

bot = telegram.Bot(token=secret_token)


def start(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    button = ReplyKeyboardMarkup([['/leave_review'], ['/find_review'], ['/help']], resize_keyboard=True)
    context.bot.send_message(
        chat_id=chat.id,
        text='Привет, {}. Я бот, который позволит тебе найти или же оставить отзыв о компаниях и даже людях!\n'
             'Давай расскажу тебе, что умею: \n'
             'При нажатии команды "/leave_review", ты можешь оставить отзыв.\n'
             'При нажатии команды "/find_review", ты можешь найти отзыв.\n'
             'Если возникнут вопросы, то ты всегда можешь нажать "/help".\n'.format(name),
        reply_markup=button
    )

def help(update, context):
    chat = update.effective_chat
    context.bot.send_message(
        chat_id=chat.id,
        text='Давай расскажу тебе подробнее про каждую из команд: \n'
             '-Команда /leave_review необходима для того, чтобы запустить процесс написания бота. \n'
             'Бот будет задавать тебе вопросы по поводу компании, по итогам которой будет сформирован отзыв. \n'
             'Если что-то перепутали или не хотите отвечать, то после каждого вопроса есть команды /skip или же /cancel. \n'
             'В конце вам нужно будет проверить корректность заполнения отзыва. \n'
             'Отзыв будет отправлен модератору и если все пройдет удачно, то ваш отзыв будет опубликован в канале, \n'
             'а если будут ошибки, то модератор отправит вам его обратно с комментарием.'
    )

def facts_to_str(user_data):
    facts = list() 
    for key, value in user_data.items():
        facts.append('{} - {}'.format(key, value))

    return "\n".join(facts).join(['\n', '\n'])


SELF_FULLNAME, COMPANY_NAME, REVIEW, PHOTO, LINK, CONFIRMATION = range(6)

def leave_review(update, context):
    update.message.reply_text(
        'Для начала необходимо узнать ваше имя.\n\n'
        'Команда /cancel, чтобы прекратить написание отзыва.')
    return SELF_FULLNAME

def self_fullname(update, context):
    user = update.message.from_user
    user_data = context.user_data
    category = 'self_fullname'
    text = update.message.text
    user_data[category] = text
    logger.info("Собственное имя %s: %s", user.first_name, update.message.text)
    update.message.reply_text('Спасибо. Пойдем дальше! \n'
                              'Теперь введите название компании о которой хотите оставить отзыв.\n\n'
                              'Команда /cancel, чтобы прекратить написание отзыва.',
                              reply_markup=ReplyKeyboardRemove(),
                              )
    return COMPANY_NAME

def company_name(update, context):
    user = update.message.from_user
    user_data = context.user_data
    category = 'company_name'
    text = update.message.text
    user_data[category] = text
    logger.info("Название компании %s: %s", user.first_name, update.message.text)
    update.message.reply_text('Отлично! Теперь напишите сам отзыв.\n\n'
                              'Команда /cancel, чтобы прекратить написание отзыва.',
                              reply_markup=ReplyKeyboardRemove(),
                              )
    return REVIEW

def review(update, context):
    user = update.message.from_user
    user_data = context.user_data
    category = 'review'
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
    category = 'link'
    text = update.message.text
    user_data[category] = text 
    logger.info("Ссылка %s: %s", user.first_name, update.message.text)
    update.message.reply_text('Спасибо вам за отзыв! Пожалуйста, проверьте информацию на корректность:'
                              '{}'.format(facts_to_str(user_data)), reply_markup=markup)

    return CONFIRMATION

def confirmation(update, context: CallbackContext):
    user_data = context.user_data
    user = update.message.from_user
    update.message.reply_text('Спасибо! Информация будет отправлена менеджеру на модерацию', reply_markup=ReplyKeyboardRemove())
    bot.send_photo(chat_id=secret_feedback_chat_id,
                   reply = update.message.reply_to_message,
                   photo=open(f'{user.first_name}_photo.jpg', 'rb'),
                   caption="Новый отзыв от пользователя {}".format(user.name) + ":\n {}".format(facts_to_str(user_data)),
                   parse_mode=telegram.ParseMode.HTML
                   )


def do_echo(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id

    if chat_id == FEEDBACK_USER_ID:
        # Смотрим на реплаи
        error_message = None
        reply = update.message.reply_to_message
        if reply:
            forward_from = reply.forward_from
            if forward_from:
                text = 'Сообщение от автора канала:\n\n' + update.message.text
                context.bot.send_message(
                    chat_id=forward_from.id,
                    text=text,
                )
                update.message.reply_text(
                    text='Сообщение было отправлено',
                )
            else:
                error_message = 'Нельзя ответить самому себе'
        else:
            error_message = 'Сделайте reply чтобы ответить автору сообщения'

        # Отправить сообщение об ошибке если оно есть
        if error_message is not None:
            update.message.reply_text(
                text=error_message,
            )
    else:
        # Пересылать всё как есть
        update.message.forward(
            chat_id=FEEDBACK_USER_ID,
        )
        update.message.reply_text(
            text='Сообщение было отправлено',
        )



def cancel(update, _):
    user = update.message.from_user
    logger.info("Пользователь %s отменил разговор.", user.first_name)
    update.message.reply_text(
        'Мое дело предложить - Ваше отказаться \n'
        'Ждем вас снова!\n\n'
        'Если хотите написать отзыв то нажмите /leave_review \n'
        'Если хотите найти отзыв то нажмите /find_review \n'
        'Во всех остальных случаях поможет /help', 
        reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():

    updater = Updater(token=secret_token)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('help', help))

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('leave_review', leave_review)],

        states={
            SELF_FULLNAME: [MessageHandler(Filters.text & ~Filters.command, self_fullname)],
            COMPANY_NAME: [MessageHandler(Filters.text & ~Filters.command, company_name)],
            REVIEW: [MessageHandler(Filters.text & ~Filters.command, review)],
            PHOTO: [MessageHandler(Filters.photo, photo), CommandHandler('skip', skip_photo)],
            LINK: [MessageHandler(Filters.text & ~Filters.command, link)],
            CONFIRMATION: [MessageHandler(Filters.regex('^Confirm$'),
                                      confirmation),
            MessageHandler(Filters.regex('^Restart$'), leave_review)
                       ]
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    updater.dispatcher.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
