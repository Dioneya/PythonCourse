import re

class StringFormater(object):
    #Удаление слов меньше чем letters_cnt букв
    def delete_words_less(self,string,letters_cnt):
        words = self.__split_string(string)
        return ' '.join([word for word in words if len(word)>=letters_cnt])

    #Заменить числа на *
    def replace_numbers(self,string):
        return ''.join(['*' if letter.isdigit() else letter for letter in string])

    #Вставка по одному пробелу между всеми символами в строке
    def add_space_between_letters(self, string):
        return ' '.join(string)

    #Сортировка слов по размеру
    def get_sorted_by_len(self, string):
        words = self.__split_string(string)
        return ' '.join(sorted(words, key=len))

    #Сортировка слов в лексикографическом порядке
    def get_sorted_by_lexgraph(self, string):
        words = self.__split_string(string)
        return ' '.join(sorted(words, key=str.lower))
    
    #Разбиение строки на слова без пунктуации
    def __split_string(self, string):
        return string.replace('; ', ' ').replace(', ', ' ').replace('. ', ' ').replace(': ',' ').split(' ')