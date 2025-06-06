# Библиотека. Второй класс


class Book:
    material = 'бумага'
    exist_text = True
    is_reserved = False


    def __init__(self, title, author, page_qty, isbn):
        self.title = title
        self.author = author
        self.page_qty = page_qty
        self.isbn = isbn


    def about(self):
        if self.is_reserved:
            print(f'Название: {self.title}, Автор: {self.author}, страниц: {self.page_qty}, материал: {self.material}, '
                  f'зарезервирована')
        else:
            print(f'Название: {self.title}, Автор: {self.author}, страниц: {self.page_qty}, материал: {self.material}')


class SchoolBook(Book):

    def __init__(self, title, author, page_qty, isbn, subject, grade, exist_exercise):
        super().__init__(title, author, page_qty, isbn)
        self.subject = subject
        self.grade = grade
        self.exist_exercise = exist_exercise


    def about(self):
        if self.is_reserved:
            print(f'Название: {self.title}, Автор: {self.author}, страниц: {self.page_qty}, предмет: {self.subject}, '
                  f'класс: {self.grade}, зарезервирована')
        else:
            print(f'Название: {self.title}, Автор: {self.author}, страниц: {self.page_qty}, предмет: {self.subject}, '
                  f'класс: {self.grade}')


school_book1 = SchoolBook('Русский язык', 'Мария Закожурникова, Николай Рождественский', 160,
                          '978-5-907844-14-8', 'Русский язык', 4, False)
school_book2 = SchoolBook('Геометрия', 'Татьяна Виноградова', 112, '978-5-04-117721-8',
                          'Математика', 7, True)
school_book3 = SchoolBook('Чтение', 'Татьяна Головкина, Светлана Ильина', 270,
                          '978-5-09-100016-0','Чтение', 6, False)


school_book1.about()
school_book2.about()
school_book3.about()

school_book2.is_reserved = True

school_book2.about()
