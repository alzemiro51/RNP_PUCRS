import random
import os
import subprocess
import sys

def split_data_set(labels_dir):

    f_val = open("plane_test.txt", 'w')
    f_train = open("plane_train.txt", 'w')
    
    path, dirs, files = next(os.walk(labels_dir))
    data_size = len(files)

    ind = 0
    data_test_size = int(0.1 * data_size)
    test_array = random.sample(range(data_size), k=data_test_size)
    
    for f in os.listdir(labels_dir):
        if(f.split(".")[1] == "txt"):
            ind += 1
            
            if ind in test_array:
                f_val.write(labels_dir[0:labels_dir.find("labels")]+'JPEGImages/'+f.split(".")[0]+'.jpg\n')
            else:
                f_train.write(labels_dir[0:labels_dir.find("labels")]+'JPEGImages/'+f.split(".")[0]+'.jpg\n')


split_data_set(sys.argv[1])
