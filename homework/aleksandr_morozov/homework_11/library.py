# Библиотека. Первый класс


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


book1 = Book('Азбука', 'Р. С. Севирина', 10, '978-5-7057-5317-8')
book2 = Book('Чебурашка', 'Анна Маслова', 160, '978-5-17-153631-2')
book3 = Book('Волшебник Изумрудного города', 'Александр Волков', 224, '978-5-17-162242-8')
book4 = Book('Гарри Поттер и философский камень', 'Джоан Кэтлин Роулинг', 432,
             '978-5-389-07435-4')
book5 = Book('Маленький принц', 'Антуан де Сент-Экзюпери', 112, '978-5-699-90130-2')

book1.about()
book2.about()
book3.about()
book4.about()
book5.about()

book3.is_reserved = True

book3.about()
