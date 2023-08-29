import logging
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler, CallbackQueryHandler)

from config import secret_token

from leave_feedback import *
from find_feedback import *
from start import start, help

from keyboards import get_activities_page_one, get_activities_page_two


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def check_callback(update, context):
    """Функция-обработчик callback запросов"""
    data = update.callback_query.data
    if data == 'all_reviews':
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
    else:
        pass


def main():

    updater = Updater(token=secret_token)
#    updater.dispatcher.add_handler(MessageHandler(Filters.regex('^Посмотреть все имена$'), get_all_workers))

#    updater.dispatcher.add_handler(CallbackQueryHandler(callback_handler))
    updater.dispatcher.add_handler(CallbackQueryHandler(check_callback))

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
