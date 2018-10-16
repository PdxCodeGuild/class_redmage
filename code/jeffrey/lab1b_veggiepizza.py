from turtle import *

# Veggie pizza in the sky over the great pyramids of Giza.

speed(0)

fillcolor('orange')
begin_fill()

i = 0
x = 25
while i < 33:
    left(45)
    forward(x)
    right(90)
    forward(x)
    left(45)
    i = i + 11
    x = x*2
    penup()
    setposition(i*2,0)
    pendown()

setposition(0,0)
end_fill()

penup()
setposition(-25,40)
pendown()
fillcolor('brown')
begin_fill()
circle(30)
end_fill()

penup()
setposition(-25,45)
pendown()

fillcolor('yellow')
begin_fill()
circle(25)
end_fill()
left(90)
forward(50)
right(180)
forward(25)
right(90)
forward(25)
right(180)
forward(50)
right(180)
forward(25)
right(45)
forward(25)
right(180)
forward(50)
right(180)
forward(25)
right(90)
forward(25)
right(180)
forward(50)

penup()
setposition(-30,55)
pendown()

edge_length = 0
i = 0
while i < 10:
    forward(edge_length)
    right(154)
    i = i+1
    edge_length += 1

penup()
setposition(-31,75)
pendown()

edge_length = 0
i = 0
while i < 10:
    forward(edge_length)
    right(154)
    i = i+1
    edge_length += 1

penup()
setposition(-23,80)
pendown()

edge_length = 0
i = 0
while i < 10:
    forward(edge_length)
    right(154)
    i = i+1
    edge_length += 1

penup()
setposition(-15,57)
pendown()

edge_length = 0
i = 0
while i < 10:
    forward(edge_length)
    right(154)
    i = i+1
    edge_length += 1

penup()
setposition(-13,71)
pendown()

edge_length = 0
i = 0
while i < 10:
    forward(edge_length)
    right(154)
    i = i+1
    edge_length += 1

penup()
setposition(-36,67)
pendown()

edge_length = 0
i = 0
while i < 10:
    forward(edge_length)
    right(154)
    i = i+1
    edge_length += 1

done()