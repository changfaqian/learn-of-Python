import turtle
turtle.setup(800,400,200,200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.seth(-45)
turtle.pencolor("purple")
for i in range(4):
    turtle.circle(40,90)
    turtle.circle(-40,90)
    if i in 2:
        turtle.pencolor("red")
turtle.circle(40,45)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)
