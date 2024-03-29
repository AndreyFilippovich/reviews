import logging
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler, CallbackQueryHandler)

from config import secret_token

from leave_review import *
from find_review import *
from start import start, help
from activity.designer import *
from registration import *
from constants.messages import PREWELCOME_MESSAGE

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

spisok = ['designer', 'target', 'manager', 'content_manager', 'marketolog', 'producer', 'blogger_manager']

def prestart(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    context.bot.send_message(
        chat_id=chat.id,
        text=PREWELCOME_MESSAGE.format(name),
        reply_markup=InlineKeyboardMarkup(subscribe_keyboard)
    )

def check_callback(update, context):
    """Функция-обработчик callback запросов"""
    data = update.callback_query.data
    if data == 'main_menu':
        start(update, context)
    elif data == 'all_reviews':
        all_reviews(update, context)
    elif data == 'my_reviews':
        my_reviews(update, context)
    elif data == 'find_by_activity':
        find_by_activity(update, context)
    elif data == 'more':
        find_by_activity_2(update, context)
    elif data == 'back':
        find_by_activity(update, context)
    elif data == 'find_by_name':
        find_by_name(update, context)
    elif data in spisok:
        find_by_prof(update, context, data)
    else:
        pass



def main():

    updater = Updater(token=secret_token)
    
    check_subscribe = CallbackQueryHandler(check_start_subscription, pattern=SUBSCRIBE)
    main_handler = CallbackQueryHandler(check_callback)
    my_reviews_handler = CallbackQueryHandler(my_reviews_callback, pattern='^reviews#')
    all_reviews_handler = CallbackQueryHandler(all_reviews_callback, pattern='^all_reviews#')
    prof_reviews_handler = CallbackQueryHandler(prof_reviews_callback, pattern=r'\w{6,15}_reviews#')

    
    updater.dispatcher.add_handler(check_subscribe)
    updater.dispatcher.add_handler(prof_reviews_handler)
    updater.dispatcher.add_handler(all_reviews_handler)
    updater.dispatcher.add_handler(my_reviews_handler)
    updater.dispatcher.add_handler(main_handler)
    

    updater.dispatcher.add_handler(CommandHandler('start', prestart))
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
