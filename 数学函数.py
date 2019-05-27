#数学功能
#返回数字绝对值
x1 = -1
x2 =abs(x1)
print(x2)
#比较两个值大小
a1 = 3
a2 = 4
print((a1>a2)-(a1<a2))
#如果输出的值为-1，则a1<a2;输出的值为1，a1>a2.输出的值为0，a1=a2

#返回给定参数的最大值和最小值
print(max(1,2,3,4,5))
print(min(1,2,3,4,5))

#求x的y次方
print(pow(2, 5))


#round(x[,n]), 四舍五入,如果给出n值则返回到小数点后n位
print(round(3.123))
print(round(3.456, 2))
print(round(3.546, 1))

#import 导入库
#库：封装一些功能
#math：数学相关的库

#向上取整
import math
print(math.ceil(18.1))
print(math.ceil(18.9))
#向下取整
import math
print(math.floor(18.2))
print(math.floor(18.9))


#返回整数部分与小数部分（元组）
print(math.modf(22.3))

#开平方
print(math.sqrt(16))

#随机数
import random
#1 从序列的元素中随机选择一个数据
print(random.choice([1,3,5,7,9,"aa"]))
#2
print(random.choice(range(5))) #range(5)=[0,1,2,3,4]
#3
print(random.choice("sunck")) #"sunck" == ["s"."u","n","c","k"]

#生成一个1~100的随机数(彩票系统）
r1 = random.choice(range(100))+1
print(r1)

#random.randrange([start,] stop[,step])
#从指定范围内，按指定的基数（step）递增的集合中选取一个随机数
#start--指定范围的开始值，包含在范围内，默认是0
#stop--指定范围的结束值，不包含在范围内
#step--指定的递增基数，默认是1
print(random.randrange(1, 100, 2))
#取1~99之间所有的奇数
print(random.randrange(100))
#从0~99选取一个随机数


#随机生成[0,1）之间的数,浮点数
print(random.random())

#将序列的所有元素随机排列
list = [1,2,3,4,5]
random.shuffle(list)
print(list)

#随机生成实数,范围为[3, 9]
print(random.uniform(3, 9))

#三角函数