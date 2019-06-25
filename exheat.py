heat=input("请输入要转换的热量：\n")
if heat[-1:]=='l':
    heat=eval(heat[0:-3])*4.186
    print("{:.3f}J".format(heat))
elif heat[-1:]=='J':
    heat=eval(heat[0:-1])/4.186
    print("{:.3f}cal".format(heat))
else:
    print("请输入正确的热量值！")
