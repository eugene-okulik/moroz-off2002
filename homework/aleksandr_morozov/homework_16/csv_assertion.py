import mysql.connector as mysql
import os
import csv
import dotenv


# Отталкиваемся от домашней папки и собираем путь до файла csv
homework_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
eugene_file_path = os.path.join(homework_path, 'eugene_okulik', 'lesson_16', 'hw_data', 'data.csv')
print(eugene_file_path)

# Распечатываем данные из csv файла
with open(eugene_file_path, newline='') as csv_file:
    file_data = csv.reader(csv_file)
    data = []
    for row in file_data:
        data.append(row)
        print(row)

# Инициализируем модуль, он загружает на время сессии системные переменные из фала .env
dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

# создаем "пульт управления"
cursor = db.cursor(dictionary=True)

select_query = f'''
SELECT s.name as 'Имя', s.second_name as 'Фамилия', g.title as 'Группа', s2.title as 'Предмет', m.value as 'Оценка',
l.title as 'Урок', b.title as 'Книга'
FROM students s
JOIN `groups` g ON s.group_id = g.id
JOIN books b ON s.id = b.taken_by_student_id
JOIN marks m ON s.id = m.student_id
JOIN lessons l ON m.lesson_id = l.id
JOIN subjets s2 ON l.subject_id = s2.id
WHERE s.id = 20833
'''

cursor.execute(select_query)
result_all = list(cursor.fetchall())
print(result_all)