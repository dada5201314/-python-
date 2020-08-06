'''
你所看到的实验文档内容，都书写在 Markdown 单元格中。如果你一不小心双击了相应单元格进入到编辑状态。
不用担心，选中相应单元格，并同样使用快捷键 Shift + Enter 执行，就可以恢复到先前的状态。
H：查看所有快捷键。
S：保存当前 Notebook 内容。
P：调出 Notebook 命令栏。
B：在当前单元格下方新建空白单元格。
M：将单元格格式转换为 Markdown。
Y：将单元格格式转换为 Code。
连续按 D+D：删除当前单元格。（慎用，推荐使用 X 剪切单元格代替，因为其可以起到删除效果，且删错了还可以粘贴回来）
连续按 I+I+I：强制中止内核（当某个单元格执行时间较长或卡住时，可以强行中止，中止后前序单元格状态依旧保留，非常好用。）
Shift + Enter：运行当前单元格内容。（当 Markdown 单元格处于编辑状态时，运行即可复原）
'''
'''
多维数组ndarray 的六个参数
shape：数组的形状。
dtype：数据类型。
buffer：对象暴露缓冲区接口。
offset：数组数据的偏移量。
strides：数据步长。
order：{'C'，'F'}，以行或列为主排列顺序。
'''

import numpy as np  # 导入 NumPy 模块
#数组的创建方法
'''
在 NumPy 中，我们使用 numpy.array 将列表或元组转换为 ndarray 数组。其方法为：
numpy.array(object, dtype=None, copy=True, order=None, subok=False, ndmin=0)
object：列表、元组等。
dtype：数据类型。如果未给出，则类型为被保存对象所需的最小类型。
copy：布尔类型，默认 True，表示复制对象。
order：顺序。
subok：布尔类型，表示子类是否被传递。
ndmin：生成的数组应具有的最小维数。'''
a = np.array([1.1, 2.2, 3.3], dtype=np.float64)  # 指定 1 维数组的数值类型为 float64
print(a,a.dtype)  # 查看 a 及 dtype 类型


'''arange() 的功能是在给定区间内创建一系列均匀间隔的值。'''
np.arange(3, 7, 0.5, dtype='float32')

'''`linspace `方法也可以像` arange `方法一样，创建数值有规律的数组。
`linspace` 用于在指定的区间内返回间隔均匀的值。其方法如下：
np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
start：序列的起始值。
stop：序列的结束值。
num：生成的样本数。默认值为50。
endpoint：布尔值，如果为真，则最后一个样本包含在序列内。序列中是否包含stop值，默认为ture
retstep：布尔值，如果为真，返回间距。
dtype：数组的类型。
'''
np.linspace(0,10,10,dtype=int)
np.linspace(0,10,10,dtype=int,endpoint=False)

'''
numpy.logscale(start, stop, num, endpoint, base, dtype)
1.  start 起始值是base ** start,幂的起始值
2.	stop 终止值是base ** stop
3.	num 范围内的数值数量，默认为50
4.	endpoint 如果为true，终止值包含在输出数组当中
5.	base 对数空间的底数，默认为10
6.	dtype 输出数组的数据类型，如果没有提供，则取决于其它参数
'''

'''ones和zeros方法
shape：用于指定数组形状，例如（1， 2）或3。
dtype：数据类型。
order：{'C'，'F'}，按行或列方式储存数组。但是打印出来都一样'''
print(np.zeros((3, 2)))
print(np.ones((3, 2)))
print(np.ones((3, 2),order='F'))




#数组基本操作


'''reshape 可以在不改变数组数据的同时，改变数组的形状。
其中，numpy.reshape() 等效于 ndarray.reshape()。reshape 方法非常简单：numpy.reshape(a, newshape)
'''
print(np.arange(10).reshape((5, 2)))

'''ravel 的目的是将任意形状的数组扁平化，变为 1 维数组。ravel 方法如下：numpy.ravel(a, order='C')
order 表示变换时的读取顺序，默认是按照行依次读取，当 order='F' 时，可以按列依次读取排序。'''
a = np.arange(10).reshape((2, 5))
print(np.ravel(a))


