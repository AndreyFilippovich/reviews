import sqlite3
import telegram

import os

from dotenv import load_dotenv

load_dotenv()

secret_token = os.getenv('TOKEN')
secret_chat_id = os.getenv('CHAT_ID')
secret_feedback_chat_id = os.getenv('FEEDBACK_USER_ID')

bot = telegram.Bot(token=secret_token)


def ensure_connection(func):
    """ Декоратор для подключения к СУБД: открывает соединение,
        выполняет переданную функцию и закрывает за собой соединение.
        Потокобезопасно!
    """
    def inner(*args, **kwargs):
        with sqlite3.connect('review.db') as conn:
            kwargs['conn'] = conn
            res = func(*args, **kwargs)
        return res

    return inner

@ensure_connection
def init_db(conn, force: bool = False):

    c = conn.cursor()

    if force:
        c.execute('DROP TABLE IF EXISTS user_review')

    c.execute('''
        CREATE TABLE IF NOT EXISTS user_review (
            id          INTEGER PRIMARY KEY,
            user_id     INTEGER NOT NULL,
            name        TEXT NOT NULL,
            worker        TEXT NOT NULL,
            activity        TEXT NOT NULL,
            review        TEXT NOT NULL,
            link        TEXT NOT NULL
        )
    ''')

    conn.commit()

@ensure_connection
def add_message(conn, user_id: int, name: str, worker: str, activity: str, review: str, link: str,):
    c = conn.cursor()
    c.execute('INSERT INTO user_review (user_id, name, worker, activity, review, link) VALUES (?, ?, ?, ?, ?, ?)', (
                                                                         user_id,
                                                                         name,
                                                                         worker,
                                                                         activity,
                                                                         review,
                                                                         link
                                                                         ))
    conn.commit()

@ensure_connection
def count_messages(conn, user_id: int):
    c = conn.cursor()
    c.execute('SELECT COUNT(*) FROM user_review WHERE user_id = ? LIMIT 1', (user_id, ))
    (res, ) = c.fetchone()
    return res

@ensure_connection
def list_messages(conn, user_id: int, limit: int = 10):
    c = conn.cursor()
    c.execute('SELECT worker, activity, review, link FROM user_review WHERE user_id = ? ORDER BY id DESC LIMIT ?', (user_id, limit))
    return c.fetchall()

@ensure_connection
def list_of_designers(conn, user_id: int, limit: int = 10):
    c = conn.cursor()
    c.execute('SELECT name, worker, activity, review, link FROM user_review WHERE activity IN Дизайн', (user_id, limit))
    return c.fetchall()

#@ensure_connection
#def get_review(conn, company_name: str):
#    c = conn.cursor()
#    c.execute('SELECT company_name FROM user_review WHERE company_name = ?', (company_name))
#    return c.fetchone()

@ensure_connection
def get_review(conn, user_id: int):
    c = conn.cursor()
    c.execute('SELECT COUNT(*) FROM user_review WHERE user_id = ? LIMIT 1', (user_id, ))
    (res, ) = c.fetchone()
    return res

