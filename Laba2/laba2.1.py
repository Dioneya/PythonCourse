def sort(d):
    list_d = list(d.items())
    list_d.sort(key=lambda i: i[1],reverse=True)
    return list_d


def read_file():
    file = open(r'C:\Users\Dioneya\Desktop\Laba2\text.txt', 'r')
    text = file.read().lower()
    out = {}
    for i in text:
        if i.isalpha():
            out[i] = 1 if out.get(i) == None else out[i]+1
    return sort(out)

print(read_file())