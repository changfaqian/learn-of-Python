import turtle
turtle.setup(800,500,200,200)
pencol=["red","orange","yellow","green",]
turtle.penup()
turtle.fd(-300)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("blue")
turtle.seth(-40)
for i in range(5):
    turtle.circle(40,80)
    turtle.circle(-40,80)
    turtle.pencolor(pencol[i-1])
turtle.circle(40,40)
turtle.fd(40)
turtle.circle(13,180)
turtle.fd(40*2/3)
