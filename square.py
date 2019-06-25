from turtle import *
i=j=0
while True:
    i+=1
    if (i%2)==0:
        j+=1
    seth(90*((i-1)%4))
    fd(5*j)
    if abs(pos())>205:
        break
    
