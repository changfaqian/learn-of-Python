from turtle import *
setup(800,500,200,100)
for i in range(3):
    seth(30+(i)*120)
    fd(100)
penup()
seth(30)
fd(100)
seth(0)
fd(-200/pow(3,1/2))
pendown()
for i in range(3):
    seth(30-(i)*120)
    fd(100)
