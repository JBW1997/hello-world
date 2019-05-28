"""
什么是字符串
字符串是以单引号或者双引号括起来的任意文本
'abc'
"def"
字符串不可变
"""
#创建字符串
str1 = "today is a good day"


"""
字符串运算
"""
#字符串连接
str2 = "today is a "
str3 = "good day"
str4 = str2 + str3
print(str4)

#输出重复字符串
str5 = "good"
str6 = str5*3
print("str6 =",str6)

#访问字符串中的某一个字符，通过索引下标查找字符，索引从0开始
#格式：字符串[下标]
str7 = "today is a good day"
print(str7[2])
#str7[2] = "s"
#print("str7 =",str7)输出错误，因为字符串不可变

#截取字符串中的一部分
#从头截取到规定下标之前,开头默认为0
str8 = "today is a good day"
print(str8[5:15])
#从头截取到规定下标之前
print(str8[:15])
#从给定下标处截取到结尾
print(str8[15:])


#判断字符串是否存在(in, not in)
str9 = "today is a good day"
print("good"in str9)
print("good1"not in str9)

#格式化输出
# %d:数字的占位符
# %s:字符串的占位符
# %f:小数的占位符
# %.nf 精确到小数点后n位，存在四舍五入
# \n:表示换行，只表示一个字符，属于转义字符
num =10
f = 12.45678
str10 = "today is a good day"
print("num = %d,f = %.2f, str10 = %s" % (num, f, str10))
print("num = %d\nstr10 = %s\nf = %.2f" % (num, str10, f))


#转义字符  \
#将一些字符转换成具有特殊含义的字符
# \n  换行
#  \\ ---> \  要想在输出的程序里得到"\"必须写成“\\”
#  \\n ---> \n
print("today is a \\n good day")
print("today is a \n good day")

#打印单引号'',转义单引号\'
#或者用双引号将单引号扩起来
# 打印双引号
print("today is a \'good\' day")
print("today is a 'good' day")
print("today is a \"good\" day")
print('today is a "good" day')

#打印多行
print("good\nnice\nman")
print("""
good
nice
man
""")

# \t 制表符   打印出来有四个空格
print("nice\tman")
# 若想打印 \\\t\\
print("\\\t\\")
print(r"\\\t\\")
#若字符串中有好多的字符串需要转义，就需要加入好多“\”
#为了简化，python允许r表示内部的字符串默认不转义


#打印路径
#C:\Users\Administrator\Desktop\python
print("C:\\Users\\Administrator\\Desktop\\python")
#当路径中包含较多的转义字符时，加“\”往往很麻烦，这是可以用“r”
print(r"C:\Users\Administrator\Desktop\python")

#windows目录下的路径
#C:\Users\Administrator\Desktop\python
#Linux目录下的路径
#C:/Users/Administrator/Desktop/python


#eval()
#功能：将字符串str当成有效的表达式来求值，并返回计算结果
num1 = eval("123")
print(num1)
print(type(num1))
print(eval("+123"))
print(eval("-123"))
print(eval("12+3"))
print(eval("12-3"))#eval返回的是求值的结果
#print(eval("12a3"))
#print(eval("a123"))
#以上的输出错误在于无法计算eval内的值

#len(str)
#返回s字符串的长度（包括空格）不包括汉字
print(len("today is a good day!"))


#str.lower()
#将字符串中的大写字母转换为小写的
str11 = "TODAY is a good day"
print(str11.lower())
print("str11 =%s"%(str11))#str11字符串并没有改变

#str.upper()
#将字符串中的小写字母转换为大写的
print(str11.upper())

#swapcase将字符串中大写的字母转换为小写的，将小写的字母转换为大写的
#str.swapcase()
print(str11.swapcase())


#capitalize()将字符串的首字母大写其他字母小写
#str.capitalize()
print(str11.capitalize())

#title将每个单词的首字母大写
#str.title()
print(str11.title())

#character char 字符
#center(width, fillchar)
#返回一个指定宽度的居中字符串，fillchar为填充的字符，默认为空格
#str.center(width[, fillchar]) 逗号后有空格
print(str11.center(40, "%"))
print(str11.center(40))

#ljust(width[, fillchar]
# 返回一个指定宽度的左对齐字符串，fillchar为填充的字符，默认为空格，l代表left
print(str11.ljust(40, "#"))


#rjust(width[, fillchar]
# 返回一个指定宽度的右对齐字符串，fillchar为填充的字符，默认为空格，r代表right
print(str11.rjust(40, "#"))

#zfill（width）
#返回一个指定宽度的右对齐字符串，前面补0, z代表zero
print(str11.zfill(40))

#str.count(str[, start][, end])
#返回字符串中str出现的次数，可以指定一个范围，默认从头到尾
str12 ="today is a very very good day"
print(str12.count("very"))
print(str12.count("very", 15, len(str12)))

#find(str[, start][, end])
#从左向右检测srr字符串是否包含在字符串中，可以指定范围，默认从头到尾
#得到的是第一次出现的下标
print(str12.find("very"))
print(str12.find("nice"))# 当没有时返回-1
print(str12.find("very", 22, len(str12)))

#rfind(str[, start][, end])
#从左向右检测srr字符串是否包含在字符串中，可以指定范围，默认从头到尾
#得到的是最后一次出现的下标
print(str12.rfind("very", 0, len(str12)))

#index(str, start=0, end=len(str))
#默认start=0，end=字符串的长度
#跟find()的功能一样，只不过当str不存在时会报一个异常，而find会报一个-1
print(str12.index("very"))
#print(str12.index("nice") 字符串中不存在“nice”会报错


#rindex()
#与rfind()一样，当找不到字符串的时候会报错
print(str12.rindex("very"))
#print(str12.rindex("nice")) 会报错

#lstrip()会截掉字符串左侧指定的字符，默认为空格
str13 = "*********today is a good day"
print(str13.lstrip("*"))

#rstrip()会截掉字符串右侧指定的字符，默认为空格
str14 = "&&&&&&today is a good day*******"
print(str14.rstrip("*"))
str15 ="    today is a good day      "
print(str15.rstrip(), "*", str15.lstrip())

#str.strip()
#截掉字符串左右两侧的指定字符，默认为空格
str16 = "*****today is a good day******"
print(str16.strip("*"))

