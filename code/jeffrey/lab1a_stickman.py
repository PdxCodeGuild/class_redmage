from turtle import *

# stickman holding a flower for his special friend

speed(0)

setposition(0,10)
forward(15)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(15)

setposition(0,0)
forward(50)
right(180)
forward(100)
right(180)
forward(50)
right(90)
forward(35)
right(45)
forward(25)
setposition(0,-35)
left(90)
forward(25)

penup()
setposition(50,0)
pendown()

right(45)
forward(10)
right(180)
forward(25)

edge_length = 0
i = 0
while i < 10:
    forward(edge_length)
    right(154)
    i = i+1
    edge_length += 1

##end of flower

penup()

setposition(-5000,0)
done()