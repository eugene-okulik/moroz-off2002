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

# и определите своего студента туда
cursor.execute(f"UPDATE students SET group_id = {group_id} WHERE id = {student_id}")

# Создайте несколько учебных предметов (subjects), создайте по два занятия для каждого предмета (lessons)
subjects = ['Архитектура данных', 'Системная аналитика']
lessons = ['1. Актуальность', '2. Основные термины']
lessons_id = []
for subject in subjects:
    cursor.execute(f"INSERT INTO subjects (title) VALUES ('{subject}')")
    subject_id = cursor.lastrowid
    for lesson in lessons:
        cursor.execute(f"INSERT INTO lessons (title, subject_id) VALUES ('{lesson}', '{subject_id}')")
        lessons_id.append(cursor.lastrowid)
print(lessons_id)

marks = ['good', 'excellent', 'passed', 'failed']
for lesson in lessons_id:
    cursor.execute(f"INSERT INTO marks (value, lesson_id, student_id) VALUES ('{mark}', '{lesson}', {student_id})")

db.commit()

db.close()
