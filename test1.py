#A41714036
import random
i=0
score=0
while i<5:
    i+=1
    x=random.randint(1,100)
    y=random.randint(1,100)
    print("{}+{}=".format(x,y))
    z=input()
    if int(z)==x+y:
        score+=20
print("Total score is:{}".format(score))
