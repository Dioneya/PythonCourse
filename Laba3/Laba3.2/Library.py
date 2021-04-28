from Book import Book

class Library(object):

    def __init__(self, adress, nubmer):
        self.__adress = adress
        self.__num = nubmer
        self.__books = []

    def __iadd__(self, other):
        if not isinstance(other, Book):
            raise ArithmeticError("Правый операнд должен быть типом Book")
        self.__books.append(other)
        return self
    
    def __iter__(self):
        self.__iter = 0
        return self

    def __next__(self):
        if self.__iter < len(self.__books): 
            x = self.__books[self.__iter] 
            self.__iter += 1
            return x
        else:
            raise StopIteration

