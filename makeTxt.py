import os
import random


trainval_percent = 0.95
train_percent = 0.95
xmlfilepath = 'data/Annotations'
txtsavepath = 'data/Imagesets'
total_xml = os.listdir(xmlfilepath)

num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

ftrainval = open('data/Imagesets/trainval.txt', 'w')
ftest = open('data/Imagesets/test.txt', 'w')
ftrain = open('data/Imagesets/train.txt', 'w')
fval = open('data/Imagesets/val.txt', 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()
