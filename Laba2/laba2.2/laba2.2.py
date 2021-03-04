import hashlib 
import os

def print_double(d):
    print("Совпадения в:")
    for i in d.values():
        if len(i) > 1:
            print(i)

def get_files_hash(path):
    result = {}
    for dirs, folder, files in os.walk(path):
        for _file in files:
            file_path = os.path.join(dirs,_file)
            file_text = open(file_path,'r').read()
            key = hashlib.md5(file_text.encode()).hexdigest()

            if result.get(key) == None: result[key] = [file_path]  
            else: result[key].append(file_path)

    print_double(result)
    

get_files_hash(r'C:\Users\Dioneya\Desktop\Laba2\laba2.2')