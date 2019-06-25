import turtle as t
import math as m
def circle(r):
    t.circle(5,360)
    while(abs(t.pos())<30):
        
        for i in range(360):
            t.circle(m.exp(i/180)*r,1)
        r=r*m.exp(2)
t.setup(1366,768,0,0)
pencol=["red","orange","yellow","green",]
t.getscreen().delay(0)
t.getscreen().tracer(0)
circle(5)


