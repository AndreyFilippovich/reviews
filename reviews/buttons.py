from telegram import ReplyKeyboardMarkup

markup = ReplyKeyboardMarkup([['Подтвердить', 'Заново']], resize_keyboard=True, one_time_keyboard=True)

main_button = ReplyKeyboardMarkup([['Оставить отзыв'], ['Найти отзыв'], ['Помощь']], resize_keyboard=True, one_time_keyboard=True)

choose_button=ReplyKeyboardMarkup([['Дизайн'], ['Таргет'], ['Менеджмент'], ['Контент-менеджер'], ['Видео-мейкер'], ['Фотограф'],
                                  ['Копирайтер'], ['Контекстная реклама'], ['Авитолог'], ['SMM-щик'], ['Разработчик чат-ботов'],
                                  ['Контент-мейкер'], ['Маркетолог'], ['Продюсер'], ['Менеджер по блогерам']], resize_keyboard=True, one_time_keyboard=True)
