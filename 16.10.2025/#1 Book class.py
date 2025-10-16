class Book: # Класс содержащий название книги, ее автора и год
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def info(self) -> str: # Ф-ция выводит строку вида: Автор "Название", год
        return f'{self.author} "{self.title}", {self.year}г.'

book1 = Book("Евгений Онегин", "А.С.Пушкин", 1833)

print(book1.info())