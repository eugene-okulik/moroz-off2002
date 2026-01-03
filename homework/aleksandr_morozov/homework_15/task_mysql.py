# Работа с БД MySQL через Python

import mysql.connector as mysql
import random


def print_cursor(func):
    for row in func:
        print(row)


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
insert_student_query = "INSERT INTO students (name, second_name, group_id) VALUES (%s, %s, NULL)"
cursor.execute(insert_student_query, (input('Имя '), (input('Фамилия '))))
# print(cursor.statement)
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
cursor.execute(
    "INSERT INTO `groups` (title, start_date, end_date) VALUES ('Created by Python', 'April 2025', 'August 2025')"
)
# print(cursor.statement)
group_id = cursor.lastrowid   # сохраняем в переменную id созданной группы

# и определите своего студента туда
cursor.execute(f"UPDATE students SET group_id = {group_id} WHERE id = {student_id}")

# Создайте несколько учебных предметов (subjects), создайте по два занятия для каждого предмета (lessons)
subjects = ['Архитектура данных', 'Системная аналитика']
lessons = ['1. Актуальность', '2. Основные термины']
lessons_id = []
marks_id = []

for subject in subjects:
    cursor.execute(f"INSERT INTO subjects (title) VALUES ('{subject}')")
    subject_id = cursor.lastrowid
    for lesson in lessons:
        cursor.execute(f"INSERT INTO lessons (title, subject_id) VALUES ('{lesson}', '{subject_id}')")
        lessons_id.append(cursor.lastrowid)
        mark = random.randint(61, 100)
        cursor.execute(
            f"INSERT INTO marks (value, lesson_id, student_id) VALUES ('{mark}', '{cursor.lastrowid}', {student_id})"
        )
        marks_id.append(cursor.lastrowid)

print('student_id', student_id, 'group_id', group_id)
print('id добавленных уроков: ', lessons_id, 'id добавленных оценок: ', marks_id)
db.commit()

cursor.execute(f"SELECT * FROM marks WHERE student_id = {student_id}")
result_marks = list(cursor.fetchall())

cursor.execute(f"SELECT * FROM books WHERE taken_by_student_id = {student_id}")
result_books = list(cursor.fetchall())

select_query = f'''
SELECT s.name as 'Имя', s.second_name as 'Фамилия', g.title as 'Группа', s2.title as 'Предмет', m.value as 'Оценка',
l.title as 'Урок', b.title as 'Книга'
FROM students s
JOIN `groups` g ON s.group_id = g.id
JOIN books b ON s.id = b.taken_by_student_id
JOIN marks m ON s.id = m.student_id
JOIN lessons l ON m.lesson_id = l.id
JOIN subjects s2 ON l.subject_id = s2.id
WHERE s.id = {student_id}
'''

cursor.execute(select_query)
result_all = list(cursor.fetchall())

print_cursor(result_marks)
print_cursor(result_books)
print_cursor(result_all)

db.close()
