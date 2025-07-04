-- Создайте студента (student)
INSERT INTO students (name, second_name, group_id) VALUES ('Alex', 'Murph', NULL);

-- Создайте несколько книг (books) и укажите, что ваш созданный студент взял их
INSERT INTO books (title, taken_by_student_id) VALUES 
	('Тайна третьей планеты', (SELECT id FROM students WHERE name = 'Alex' AND second_name = 'Murph')),
	('Изучаем Python', (SELECT id FROM students WHERE name = 'Alex' AND second_name = 'Murph'));

-- Создайте группу (group)
INSERT INTO `groups` (title, start_date, end_date) VALUES ('Python automation', 'April 2025', 'August 2025');

-- и определите своего студента туда
UPDATE students SET group_id = (SELECT id FROM `groups` WHERE title = 'Python automation' AND start_date = 'April 2025' AND end_date = 'August 2025') 
	WHERE name = 'Alex' AND second_name = 'Murph';

-- Создайте несколько учебных предметов (subjects)
INSERT INTO subjects (title) VALUES ('Философия_Alex'), ('Начертательная геометрия_Alex');

-- Создайте по два занятия для каждого предмета (lessons)
INSERT INTO lessons (title, subject_id) VALUES 
	('Урок 1. Введение в Филисофию', (SELECT id from subjeсts s WHERE title = 'Философия_Alex')), 
	('Урок 2. История Филисофии', (SELECT id from subjeсts s WHERE title = 'Философия_Alex')),
	('Урок 1. Стандарты и шаблоны', (SELECT id from subjeсts s WHERE title = 'Начертательная геометрия_Alex')),
	('Урок 2. Техника создания чертежа', (SELECT id from subjeсts s WHERE title = 'Начертательная геометрия_Alex'));

-- Поставьте своему студенту оценки (marks) для всех созданных вами занятий
INSERT INTO marks (value, lesson_id, student_id) VALUES
	('99', (SELECT id FROM lessons WHERE title = 'Урок 1. Введение в Филисофию'), (SELECT id FROM students WHERE name = 'Alex' AND second_name = 'Murph')),
	('100', (SELECT id FROM lessons WHERE title = 'Урок 2. История Филисофии'), (SELECT id FROM students WHERE name = 'Alex' AND second_name = 'Murph')),
	('50', (SELECT id FROM lessons WHERE title = 'Урок 1. Стандарты и шаблоны'), (SELECT id FROM students WHERE name = 'Alex' AND second_name = 'Murph')),
	('46', (SELECT id FROM lessons WHERE title = 'Урок 2. Техника создания чертежа'), (SELECT id FROM students WHERE name = 'Alex' AND second_name = 'Murph'));

-- 1. Все оценки студента
SELECT * FROM marks WHERE student_id = 20798

-- 2. Все книги, которые находятся у студента
SELECT * FROM books WHERE taken_by_student_id = 20798

-- 3. Для вашего студента выведите всё, что о нем есть в базе: группа, книги, оценки с названиями занятий и предметов
SELECT s.name as 'Имя', s.second_name as 'Фамилия', g.title as 'Группа', s2.title as 'Предмет', m.value as 'Оценка', l.title as 'Урок', b.title as 'Книга'
FROM students s 
JOIN `groups` g ON s.group_id = g.id
JOIN books b ON s.id = b.taken_by_student_id
JOIN marks m ON s.id = m.student_id
JOIN lessons l ON m.lesson_id = l.id
JOIN subjeсts s2 ON l.subject_id = s2.id
WHERE s.name = 'Alex' AND s.second_name = 'Murph'

-- без книг
SELECT DISTINCT s.name as 'Имя', s.second_name as 'Фамилия', g.title as 'Группа', s2.title as 'Предмет', m.value as 'Оценка', l.title as 'Урок'
FROM students s 
JOIN `groups` g ON s.group_id = g.id
JOIN books b ON s.id = b.taken_by_student_id
JOIN marks m ON s.id = m.student_id
JOIN lessons l ON m.lesson_id = l.id
JOIN subjeсts s2 ON l.subject_id = s2.id
WHERE s.name = 'Alex' AND s.second_name = 'Murph'

