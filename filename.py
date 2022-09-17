 # -*- coding: utf-8 -*-

import os

def replace_suffix(filedir, suffix):
     files = os.listdir(filedir)
     num = 0
     for filename in files:
      portion = os.path.splitext(filename)
      if portion[1] != suffix:
        newname =  suffix + portion[0]+ portion[1]
        filename = filedir + '\\' +filename
        newname = filedir + '\\' +newname
        os.rename(filename, newname)
        print("替换文件后缀", filename)
        num = num + 1
        print(num)

if __name__ == '__main__':
     replace_suffix('C:\\Users\\asus\\Desktop\\新建文件夹', '1')
