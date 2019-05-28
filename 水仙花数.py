num = int(input("请输入一个三位数："))
a = num % 10
b = num // 10 % 10
c = num // 100
if a**3 + b**3 + c**3 ==num:
    print("是水仙花数")
else:
    print("不是水仙花数")