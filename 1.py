#A41714036
fa=eval(input("请输入父亲身高:"))
ma=eval(input("请输入母亲身高:"))
gen=input("请输入性别:")
if (gen=='男'):
    high=(ma+fa)*1.08/2
elif (gen=='女'):
    high=(fa*0.923+ma)/2
else:
    print("请输入正确性别！")
print("{:.2f}".format(high))
