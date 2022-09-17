import os

rootdir = 'C:\\Users\\asus\\Desktop\\新建文件夹'

img_file_l = []
img_dir_l = []

for parent, dirnames, filenames in os.walk(rootdir):
    for img_one in filenames:
        # old_name = img_one.split('/')[-1]
        new_name = img_one.replace(" ", "") #此处可以自行修改变成去除空格or去除逗号等等
        new_name = os.path.join(rootdir, new_name)
        old_name = os.path.join(rootdir, img_one)
        print(old_name)
        print(new_name)
        os.rename(old_name, new_name)