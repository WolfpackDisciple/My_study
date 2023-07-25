# остановился на 4 м уроке

import sqlite3 as sq

with sq.connect("data_tutorial2.db") as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
            name TEXT,
            sex INTEGER,
            old INTEGER,
            score INTEGER
            )""")
    #cur.execute("""INSERT INTO users VALUES('Sasha', 1, 30, 321)""")
    #cur.execute("""INSERT INTO users VALUES('Katya', 2, 20, 21421)""")
    cur.execute("""SELECT * FROM users WHERE score > 150 ORDER BY score DESC LIMIT 5""")
    #result = cur.fetchall() # Для получение результата отбора sql запроса
    #print(result)
    #for result in cur:
     #   print(result)  # отобразить в упорядоченном формате(последовательный отбор)

    result2 = cur.fetchmany(2) # возвращает количество записей не более чем указаггл
    result3 = cur.fetchone() # первая запись
    print(result2)
    print(result3)
"""INSERT INTO users (name, old, score) VALUES('Fedor', 32, 200) - Передать новые данные"""
"""INSERT INTO users VALUES('Mihail', 1, 19, 200) - Передать новые данные"""

"""SELECT name, old, score FROM users -запрос показывает содержимое ячеек"""
"""SELECT * FROM users все поля в табице"""
"""SELECT *  FROM users WHERE score < 1000 Показывает запись шде очки меньше 1000"""
"""SELECT *  FROM users WHERE socore BETWEEN 500 AND 1000 - выбрать все записи в интервале от 500 до 1000"""