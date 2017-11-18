### 一、基本数据类型

					整型 int
			数字(Number)    浮点型 float
					布尔型 bool
					复数 complex
			
	Python基本数据类型		字符串 str 不可变  |
				序列	列表 list	  |--有序、可用下标索引来访问，支持切片[start:end]
					元组 tuple	  |
			组
				集合	set 无序、无索引、不可切片
					
				字典	dict key、value键值对是其最基本概念


	int str tuple 值类型 不可变
	list set dict 引用类型 可变


### 二、运算符
		算术运算符 + - * / // % **
		赋值运算符 = += -= *= /= %= //= **=
		比较(关系)运算符 == != >= > < <=
		逻辑运算符 and or not (not > and > or)
		((not a) or ((b + 2) == c)) == (not a or b + 2 == c)
		>>> 1 and 3
		3 --> 逻辑”与“看第二个值是否为True，是则返回第二个
		>>> 1 or 2
		1 --> 逻辑“或”首个值若为True即返回首个，若第二个为True返回第二个，否则返回False
		>>> 0 or 3
		3
		>>> not 5
		False

		成员运算符 in 、not in
		身份运算符 is 、is not --> 对象的三个特征：id value type，以下为三种类型比较
		>>> a = 1
		>>> b = 1.0
		>>> a == b
		True

		>>> a is b
		False
		>>> hex(id(a)), hex(id(b))
		('0xa6b040', '0x7ff8ae35d198')
		>>> a = 1
		>>> b = 1
		>>> a is b
		True
		>>> hex(id(a)), hex(id(b))                                         ('0xa6b040', '0xa6b040')

		>> a = {'a':1}
		>>> isinstance(a, int)
		False
		>>> isinstance(a, (int, dict, float))
		True --> type()不能像isinstance获取实例子类类型

		位(二进制)运算符 & | ^ ~ << >>
