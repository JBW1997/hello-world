"""
#分类：整数、浮点数、复数
#整数：python可以处理任意大小的整数
"""
#交互式复赋值定义变量
num1, num2 =1, 2
print(num1,num2)
#连续定义多个变量
num3 =1
num5 =num4 =num3
print(num3, num4, num5)
"""
浮点数：由整数和小数组成，浮点数可能会有四舍五入的误差
"""
f1 = 1.1
f2 = 2.2
print(f1 + f2)
"""
复数：由实部和虚部组成，a+bj
"""
#数字类型转换
print(int(1.11))
print(float(1))
print(int("123"))
print(float("12.3"))
print(int("+123")) #加减号是做为正负号
#print(int("12+3")) 报错
#如果有其他无用字符会报错