# Работа с БД MySQL через Python

import mysql.connector as mysql

# задаем параметры подключения в БД
db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

# создаем "пульт управления"
cursor = db.cursor(dictionary=True)

# Создайте студента (student)
insert_student_query = "INSERT INTO students (name, second_name, group_id) VALUES (%s, %s, NULL);"
cursor.execute(insert_student_query, (input('name: '), input('second_name: ')))
student_id = cursor.lastrowid   # сохраняем в переменную id созданного студента

# Создайте несколько книг (books) и укажите, что ваш созданный студент взял их
insert_books_query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
cursor.executemany(
    insert_books_query, [
        ('Путь к Основанию', student_id),
	    ('Позитронный человек', student_id)
    ]
)

# Создайте группу (group)
cursor.execute("INSERT INTO `groups` (title, start_date, end_date) VALUES ('Created by Python', 'April 2025', "
               "'August 2025'")
group_id = cursor.lastrowid   # сохраняем в переменную id созданной группы


data = cursor.fetchall()
print(data)
print(cursor.fetchone())

db.commit()

db.close()
