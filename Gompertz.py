from math import *
t=[2,3,4,5,6,7,8,9,10]
y=[4.9,6.02,7.00,7.50,8.10,8.25,8.51,9.27,10.23]
m=int(len(t)/3)
st1,st2,st3,sy1,sy2,sy3=0,0,0,0,0,0
for i in range(m):
    st1+=t[i]
    st2+=t[i+m]
    st3+=t[i+2*m]
    sy1+=log(y[i])
    sy2+=log(y[i+m])
    sy3+=log(y[i+2*m])
st1,st2,st3,sy1,sy2,sy3=st1/m,st2/m,st3/m,sy1/m,sy2/m,sy3/m
#print(st1,st2,st3,sy1,sy2,sy3)
tb=pow((sy3-sy2)/(sy2-sy1),1/m)
tk1=(sy1*pow(tb,m)-sy2)/(pow(tb,m)-1)
ta1=(sy2-sy1)/(pow(tb,(m+1)/2)*(pow(tb,m)-1))
print(sy1,sy2,sy3,'\n',tb,tk1,ta1)
k=exp(tk1)
a=exp(ta1)
print(k,a)
for i in range(2,12):
    y=k*pow(a,pow(tb,i))
    print(y)
