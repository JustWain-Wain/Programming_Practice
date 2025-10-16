class Book: # Класс содержащий название книги, ее автора и год
    def __init__(self, title, author, year: int):
        self.title = title
        self.author = author
        self.year = year

    def info(self) -> str: # Ф-ция выводит строку вида: Автор "Название", год
        return f'{self.author} "{self.title}", {self.year}г.'

class Ebook(Book): # Класс содержащий название электронной книги, ее автора и год
    def __init__(self, title, author, year: int):
        super().__init__(title, author, year)
        self.format = "Электронная книга"

    def info(self) -> str: # Ф-ция выводит строку вида: Автор "Название", год
        return f'{self.format}: {self.author} "{self.title}", {self.year}г.'

book1 = Book("Евгений Онегин", "А.С.Пушкин", 1833)
book2 = Ebook("Гарри Поттер", "Дж. Роулинг", 1997)

print(book1.info())
print(book2.info())