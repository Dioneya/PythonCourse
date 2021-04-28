from Library import Library
from Book import Book

lib = Library(1, '51 Some str., NY')
lib += Book('Leo Tolstoi', 'War and Peace')
lib += Book('Charles Dickens', 'David Copperfield')
for book in lib:
    # вывод в виде: [1] L.Tolstoi ‘War and Peace’
    print(book)
    # вывод в виде: [‘War’, ‘Peace’]
    print(book.tag())
