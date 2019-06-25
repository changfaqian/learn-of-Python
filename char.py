ch=input("请输入一个字符:")
if ord(ch)>=48 and ord(ch)<=57:
    print("这是一个数字！")
elif ord(ch)>=65 and ord(ch)<=90:
    print("这是一个大写字母！")
elif ord(ch)>=97 and ord(ch)<=122:
    print("这是一个小写字母！")
else:
    print("这是一个其他字符!")
