import logging.config
import os

import sentry_sdk


BASE_PATH = os.path.dirname(os.path.dirname(__file__))

TG_TOKEN = "5535770400:AAHncHHXgjCv9TOHWMlm1LGUe5pRvMpD-J4"




FEEDBACK_USER_ID = 747362404

# Логирование
LOGGING = {
    'disable_existing_loggers': True,
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(module)s.%(funcName)s | %(asctime)s | %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}
logging.config.dictConfig(LOGGING)

