import sys
import argparse
import os
from datetime import *
import time 

def create_parser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('--source', default='')
    parser.add_argument ('--days', type= int,default=0)
    parser.add_argument ('--size', type= int, default=0)
    return parser

def try_to_small(file_path,_file):
    if not os.path.exists(namespace.source+'/Small'):
        os.makedirs(namespace.source+'/Small')

    if os.path.getsize(file_path) >= namespace.size: return
    os.replace(file_path, namespace.source+'/Small/'+_file)
    pass

def try_to_archive(file_path,_file):
    if not os.path.exists(namespace.source+'/Archive'):
        os.makedirs(namespace.source+'/Archive')

    maxdays = timedelta(namespace.days)
    mtime = datetime.fromtimestamp(os.path.getmtime(file_path))

    if mtime - datetime.now() < maxdays: return False
    os.replace(file_path, namespace.source+'/Archive/'+_file)
    return True

def sort_file_list():
    file_list = os.listdir(namespace.source)
    for _file in file_list:
        file_path = namespace.source+'/'+_file

        if not try_to_archive(file_path,_file):
            try_to_small(file_path,_file)
        

if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    sort_file_list()
