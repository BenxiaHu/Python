# Numpy基础语法

## 安装numpy
pip install numpy
import numpy as np



## 使用np.array()创建
np.arange(x)为左闭右开结构，数据从0开始，到x-1结束，生成规则递增序列，同时也可以指定arange的3s参数，start、stop与step。
numpy默认ndarray的所有元素的类型是相同的。
如果传进来的列表中包含不同的类型，则统一为同一类型，优先级：**str>float>int**。

### ndarray的属性
#### ndim:维度
#### shape：形状（各维度的长度）
#### size：大小（总长度）
#### dtype：元素类型

### ndarray的基础操作

#### 索引与切片：
一维数组的单元素索引跟python序列（列表，元组）完全一样，它从零开始，并且接受负索引来从数组的结尾进行索引
如果索引索引数量少于维度的多维数组，则会得到一个子维数组

#### 变形
使用reshape函数，注意参数是一个tuple
转置矩阵 np.T

#### 级联

##### np.concatenate()
参数是列表：一定要加中括号或小括号
维度必须相同
形状相符
通过axis参数改变级联的方向

##### np.hstack与np.vstack
水平级联与垂直级联,处理自己，进行维度的变更

#### 切分

##### np.split
##### np.vsplit
##### np.hsplit

#### 副本
copy()函数创建副本

#### ndarray的聚合操作

##### np.sum
求和
##### np.max/ np.min
最大最小值

#### ndarray的排序

##### 快速排序
np.sort()与ndarray.sort()
np.sort()不改变输入
ndarray.sort()本地处理，不占用空间，但改变输入

##### 唯一值,去重
np.unique()

##### 部分排序
###### np.partition(a,k)
当k为正时，我们想要得到最小的k个数
当k为负时，我们想要得到最大的k个数



## 使用内置函数便捷创建

### np.arange()
创建递增序列

### np.ones(shape=,dtype=)
创建全为1的数组矩阵

### np.zeros(shape=,dtype=)
创建全为0的数组

### np.eye(M)
创建对角线为1，其余为0 的数组

### np.full(shape=,fill_value=)
任意填充数字

### np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
线性区间等分，linspace是左闭右闭

## 使用随机库函数创建

### np.random.rand()
产生[0,1]的浮点随机数,括号里面的参数可以指定产生数组的形状

### np.random.random(size)
生成0-1的随机数,左闭右开，size表示个数，可以是一维、二维或者三维

### np.random.randint(low=,hight=,size=)
生成整数类型的随机数,low最小值，hight最大值，size个数

### np.random.randn(size)
生成标准正态分布,size个数

### np.random.normal(loc,scale,size)
生成非标准正态分布

### np.random.uniform()
均匀分布

### np.random.poisson()
泊松分布 参数λ是单位时间(或单位面积)内随机事件的平均发生次数，它适合于描述单位时间内随机事件发生的次数。

## Reference:
1. Python学习教程：Numpy系列，创建数组的三大绝招 (https://www.jianshu.com/p/7ae6947f722a)
2. Numpy (https://www.jianshu.com/p/ddb9c280666e)

