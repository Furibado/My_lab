class Book:

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return(f'Название книги: {self.title}; автор: {self.author}; год издания: {self.year}')

lolita = Book("Лолита", "Владимир Набоков", 1955)
print(lolita.get_info())



