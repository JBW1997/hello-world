num = int(input("请输入一个五位数："))
a1 = num % 10
a2 = num % 100 // 10
a3 = num // 1000% 10
a4 = num // 10000
if a1*10 + a2 == a4*10 + a3:
    print("是回文数")
else:
    print("不是回文数")
