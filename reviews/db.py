import sqlite3
import telegram

import os

from dotenv import load_dotenv

load_dotenv()

from config import *



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
            photo        TEXT NOT NULL,
            link        TEXT NOT NULL
        )
    ''')

    conn.commit()


@ensure_connection
def add_message(conn, user_id: int, name: str, worker: str, activity: str, review: str, photo: str, link: str,):
    c = conn.cursor()
    c.execute('INSERT INTO user_review (user_id, name, worker, activity, review, photo, link) VALUES (?, ?, ?, ?, ?, ?, ?)', (
                                                                         user_id,
                                                                         name,
                                                                         worker,
                                                                         activity,
                                                                         review,
                                                                         photo,
                                                                         link
                                                                         ))
    conn.commit()

# ----------------- Отзывы пользователя -----------------

@ensure_connection
def count_of_users_messages(conn, user_id: int):
    c = conn.cursor()
    c.execute('SELECT COUNT(*) FROM user_review WHERE user_id = ?', (user_id, ))
    (res, ) = c.fetchone()
    return res

@ensure_connection
def list_of_user_messages(conn, user_id: int, limit: int = 5, offset: int = '1'):
    c = conn.cursor()
    c.execute('SELECT name, worker, activity, review, photo, link FROM user_review WHERE user_id = ? ORDER BY id DESC LIMIT ? OFFSET ?', (user_id, limit, offset))
    return c.fetchall()


# ----------------- Все отзывы -----------------

@ensure_connection
def count_of_all_messages(conn, ):
    c = conn.cursor()
    c.execute('SELECT COUNT(*) FROM user_review', ())
    (res, ) = c.fetchone()
    return res

@ensure_connection
def list_of_all_messages(conn, limit: int = 5, offset: int = '1'):
    c = conn.cursor()
    c.execute('SELECT name, worker, activity, review, photo, link FROM user_review ORDER BY id DESC LIMIT ? OFFSET ?', (limit, offset))
    return c.fetchall()

# ----------------- Отзывы по профессиям -----------------

@ensure_connection
def count_of_activities(conn, activities = ''):
    c = conn.cursor()
    c.execute('SELECT COUNT(*) FROM user_review WHERE activity = ?', (activities, ))
    (res, ) = c.fetchone()
    return res


@ensure_connection
def list_of_activities(conn, activities = '', limit: int = 1, offset: int = '1'):
    c = conn.cursor()
    c.execute('SELECT name, worker, activity, review, photo, link FROM user_review WHERE activity = ? ORDER BY id DESC LIMIT ? OFFSET ?', (activities, limit, offset))
    return c.fetchall()






@ensure_connection
def get_all_reviews(conn, worker = '', limit: int = 10, offset: int = '20'):
    c = conn.cursor()
    c.execute('SELECT worker FROM user_review ORDER BY id DESC LIMIT ? OFFSET ?', (worker, limit, offset))
    return c.fetchall()


@ensure_connection
def list_of_workers(conn, worker = '', limit: int = 10):
    c = conn.cursor()
    c.execute('SELECT name, worker, activity, review, photo, link FROM user_review WHERE worker = ? ORDER BY id DESC LIMIT ?', (worker, limit))
    return c.fetchall()
