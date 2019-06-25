menoy=input("请输入要转换的钱币，美元以d或D结尾，人民币以c或C结尾\n")
if menoy[-1] in ['d','D']:
    c=eval(menoy[0:-1])*6
    print("对应的人民币为{:.2f}元".format(c))
elif menoy[-1] in ['c','C']:
    d=eval(menoy[0:-1])/6
    print("对应的美元为{:.2f}美元".format(d))
else :
    print("输入格式错误")
