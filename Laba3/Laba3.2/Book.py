from Taggable import Taggable

class Book(Taggable):
    books_cnt = 0

    def __init__(self, name, author):
        try:
            if name == None or author == None:
                raise ValueError
            Book.books_cnt+=1
            self.__name = name
            self.__author = author
            self.__code = Book.books_cnt

        except ValueError:
            print('Пустое значение')
        
    def __str__(self):
        return '[{}] {}.{} ‘{}’'.format(self.__code,self.__author[0],self.__author.split(' ')[1:],self.__name)

    def tag(self):
        return [i for i in self.__author.split(' ') if i.isalpha() and i.istitle()]