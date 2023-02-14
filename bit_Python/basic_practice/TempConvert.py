TempStr = input("请输入带有符号的温度值:")  # 定义变量TempStr接收输入的内容

if TempStr[-1] in ['F,' 'f']:  # 判断TempStr这个字符串变量中的倒数第一位是否为F或f
    C = (eval(TempStr[0:-1]) - 32)/1.8
    print("转换后的温度是{:.2f}C".format(C))
elif TempStr[-1] in ['C', 'c']:  # 如果不是F或f,再判断TempStr这个字符串变量中的倒数第一位是否为C或c
    F = 1.8*eval(TempStr[0:-1]) + 32
    print("转换后的温度是{:.2f}F".format(F))
else:
    print("输入格式错误")

