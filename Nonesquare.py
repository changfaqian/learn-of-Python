from turtle import *
setup(800,500,200,100)
penup()
fd(-100)
pendown()
for i in range(4):
    seth((i)*90)
    penup()
    fd(50)
    pendown()
    fd(100)
    penup()
    fd(50)
    pendown()



