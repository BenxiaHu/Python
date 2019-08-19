# Numpy基础语法

## 安装numpy
pip install numpy


## 使用np.array()创建
np.arange(x)为左闭右开结构，数据从0开始，到x-1结束，生成规则递增序列，同时也可以指定arange的3s参数，start、stop与step。
numpy默认ndarray的所有元素的类型是相同的。
如果传进来的列表中包含不同的类型，则统一为同一类型，优先级：**str>float>int**。 <font size=4 color=#D2691E>列表:</font>

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

### np.linspace(start,stop,num)
线性区间等分，linspace是左闭右闭

## 使用随机库函数创建

### np.random.random(size)
生成0-1的随机数,左闭右开，size表示个数，可以是一维、二维或者三维

### np.random.randint(low=,hight=,size=)
生成整数类型的随机数,low最小值，hight最大值，size个数

### np.random.randn(size)
生成标准正态分布,size个数

### np.random.normal(loc,scale,size)
生成标准正态分布


## Rference:
Python学习教程：Numpy系列，创建数组的三大绝招 (https://www.jianshu.com/p/7ae6947f722a)
