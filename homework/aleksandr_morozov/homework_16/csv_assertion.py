import mysql.connector as mysql
import os
import csv
import dotenv

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

# Отталкиваемся от домашней папки и собираем путь до файла csv
homework_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
eugene_file_path = os.path.join(homework_path, 'eugene_okulik', 'lesson_16', 'hw_data', 'data.csv')
print(eugene_file_path)

# Распечатываем данные из csv файла
with open(eugene_file_path, newline='') as csv_file:
    reader = csv.DictReader(csv_file)
    missing_data = []  # Список для хранения отсутствующих данных

    # Проверяем каждую строку файла
    for row in reader:
        # Выводим строку из файла
        print(f'\nОбрабатывается следующая строка файла:\n{row}\n')
        # Формируем SQL-запрос для проверки существования записи в базе данных
        select_query = f'''
        SELECT COUNT(*) FROM students s
        JOIN `groups` g ON s.group_id = g.id
        JOIN books b ON s.id = b.taken_by_student_id
        JOIN marks m ON s.id = m.student_id
        JOIN lessons l ON m.lesson_id = l.id
        JOIN subjects s3 ON l.subject_id = s3.id
        WHERE s.name=%s AND s.second_name=%s AND g.title=%s 
        AND b.title=%s AND s3.title=%s 
        AND l.title=%s AND m.value=%s
        '''
        # Подставляем параметры в запрос и выводим полный запрос
        params = (
            row['name'], row['second_name'], row['group_title'],
            row['book_title'], row['subject_title'], row['lesson_title'], row['mark_value']
        )
        # Ручное формирование полной версии запроса для вывода
        formatted_query = select_query % tuple(params)
        print(f'Запрос к БД:\n{formatted_query}\n')

        # Выполняем запрос с параметрами из текущего ряда CSV
        cursor.execute(select_query, params)
        result = cursor.fetchone()
        # Метод fetchone() возвращает словарь, поскольку установлен флаг dictionary=True
        # при создании курсора. То есть, вместо обычного кортежа возвращается словарь,
        # ключи которого соответствуют именам столбцов из таблицы. Поскольку запрос
        # возвращает единственный столбец с результатом агрегированной функции, нужно
        # обращаться по ключу, соответствующему этому столбцу («COUNT(*)»)
        count = result.get("COUNT(*)") or 0

        if count == 0:
            missing_data.append(list(row.values()))

    # Печать результата
    if len(missing_data) > 0:
        print("\nСледующие данные отсутствуют в базе данных:")
        for record in missing_data:
            print(record)
    else:
        print("\nВсе данные из файла присутствуют в базе данных.")

    # Закрытие соединения с базой данных
    cursor.close()
    db.close()
