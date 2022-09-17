'''
画loss图的代码，前提是results.txt文档中只能是数字
我的第一列是epoch是0/99，1/99，2/99...的格式，需要改成0，1，2，3...
第二列是0.396G的格式，需要把G去掉
第六列是loss值
'''
import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
data1_loss =np.loadtxt("F:/OCR/新建文件夹/chenming/yolov5-master/data/results.txt")
data_loss=data1_loss.strip('/')
print(data_loss)

 # x = data1_loss[:,0]   #冒号左边是行范围，冒号右边列范围。取第一列
# y = data1_loss[:,5]   #取第六列
# fig = plt.figure(figsize = (7,5))       #figsize是图片的大小`
# ax1 = fig.add_subplot(1, 1, 1) # ax1是子图的名字`
# pl.plot(x,y,'r-',label=u'result')

# ‘’g‘’代表“green”,表示画出的曲线是绿色，“-”代表画的曲线是实线，可自行选择，label代表的是图例的名称，一般要在名称前面加一个u，如果名称是中文，会显示不出来，目前还不知道怎么解决。
# p2 = pl.plot(x1, y1,'r-', label = u'RCSCA_Net')
#显示图例
# p3 = pl.plot(x2,y2, 'b-', label = u'SCRCA_Net')

# pl.legend()
# pl.xlabel(u'epoch')
# pl.ylabel(u'loss')
# plt.title(' loss for yolov5 models in training')
# plt.show()
