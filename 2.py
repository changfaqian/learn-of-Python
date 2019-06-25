a=eval(input("请输入边长一:"))
b=eval(input("请输入边长二:"))
c=eval(input("请输入边长三:"))
if (a+b<=c) or (b+c<=a) or (a+c<=b):
    print("这不是个三角形")
elif a==b==c:
    print("这是个等边三角形")
elif a==b or a==c or b==c:
    print("这是个等腰三角形")
else:
    print("这是个普通三角形")
