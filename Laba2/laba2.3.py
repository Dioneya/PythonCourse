import glob
import os
def write_to_file(path,li):
    f = open(path+'\\text.txt', 'w')
    i = 0
    while i < len(li):
        text = '{}{} {} \n'.format(0 if i <10 else '', i+1, li[i][:-4]) 
        f.write(text)
        i+=1
    f.close()
    
def get_audio_list(path):
    res = [i.split('\\')[-1] for i in glob.glob(path+'/*.mp3')]
    write_to_file(path,res)
    return res
    
path_to_audios = r'...' #Вставить свой путь
print(get_audio_list(path_to_audios)) 
