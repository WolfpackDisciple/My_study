"""Ok! Here i will write all process studing Structured Query Language"""
# On first step we dowloanded program from https://sqlitebrowser.org/

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

    cur.execute("""
    """)    #  выполнить какой либо sql  запрос

# Контекстный менеджер with автоматически закрывает
# БД даже если произошла ошибка

