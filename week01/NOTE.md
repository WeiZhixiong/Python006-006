学习笔记
=======
Python 基本数据类型
-----------------
##### 数据类型之 None
- 定义：<br/>
表示空值，通过内置名称 None 访问，逻辑值为假。
- 赋值操作：
```
a = None
```
##### 数据类型之 numbers
- 定义：<br/>
numbers 包含整型(int)、布尔型(bool)、浮点型(float)、复数(complex)
- 赋值操作：
```
a = 9 # int
b = 9.0 # float
c = True # bool
d = False # bool
b = 3 - 5j # complex
```
##### 数据类型之 Sequences
- 定义：<br/>
此类对象表示以非负整数作为索引的有限有序集。
包括可变序列和不可变序列。<br/>
不可变序列类型的对象一旦创建就不能再改变，
不可变序列包括字符串、元组和字节串。<br/>
可变序列包括列表和字节数组。
- 赋值操作：
```
fruit = ["apple", "banana"] # 列表
x = ("a", "b", "c") # 元组
y = "test string" # 字符串
z = b'abc' #字节串
```
##### 数据类型之 Set types
- 定义：<br/>
表示由不重复且不可变对象组成的无序且有限的集合
- 赋值操作：
```
s = set() # set
```
##### 数据类型之 Mappings
- 定义：<br/>
表示由任意索引集合所索引的对象的集合
- 赋值操作：
```
score = {"xiaoming": 90, "xiaoli": 91} # dict
```
##### 数据类型之 Callable types
- 定义：<br/>
此种类型可以被调用，包括函数和类
- 赋值操作：
```
# 函数
def test():
    print("hello world")
```

