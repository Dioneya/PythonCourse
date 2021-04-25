import re 

def get_text_in_file(name):
    try:
        with open (r"C:\Users\Dioneya\Desktop\Laba2\laba2.4\{}.txt".format(name), 'r') as f:
            return f.readlines()
    except IOError as err:
        print(err)
        return []
    pass

def find_matches_in_lines(lines):
    regex = r'[(]\d{3}[)](\d{7}|\d{3}([-]\d{2}){2})' # (000)1234567 или (000)111-22-33

    line_cnt = 1
    for i in lines:
        for match in re.finditer(regex, i):
            print('Строка {}, позиция {} : найдено \'{}\''.format(line_cnt, match.start(), match.group()))
        line_cnt+=1
        pass
    pass

find_matches_in_lines(get_text_in_file('text'))