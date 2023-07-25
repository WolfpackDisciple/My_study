"""Как на Python осуществляется связь с базой данных  SQlite"""
"""расширение для хранилища используют следущиерасширения
.db, .db3, .sqlite, .sqlite3"""
import sqlite3 as sq

"""
con = sq.connect("new_data_base.db")  # Здесь будет создаваться база данных, а если она уже
# есть то будет устанавливаться с ней связь

# Для неопсредственного взаимодействия с БД мы используем метод Cursor
cur = con.cursor()  # Возващает cursor

cur.execute("""
""")

con.close()  # После работы с БД ее обязательно в конце необходимо закрыть

"""


# открывать БД лучще через контекст менеджера

with sq.connect("new_data_base.db") as con:
    cur = con.cursor()
    #  выполнить какой либо sql  запрос execute("""
    #     """)
    """
    cur.execute("""#CREATE TABLE users (
        #name TEXT,
        #sex INTEGER,
        #old INTEGER,
       # score INTEGER
        #)""")   # создаем таблицу с именем users и структурой
    cur.execute("""DROP TABLE IF EXISTS users""")
    # if  not exists если не существует таб то она создается
    cur.execute("""CREATE TABLE  IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,        
            name TEXT NOT NULL,
            sex INTEGER NOT NULL DEFAULT 1,
            old INTEGER,
            score INTEGER
            )""")  # создаем таблицу с именем users и структурой

#  DEFAULT 1 - дефолтное значение , NOT NULL - не должно быть пустым,
#  PRIMARY KEY - это поле явл  главным ключем AUTOINCREMENT добавляет еденицу + чтобы сохр уникальность

# Контекстный менеджер with автоматически закрывает
# БД даже если произошла ошибка
