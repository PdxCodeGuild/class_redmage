import turtle as tur

# Veggie pizza in the sky over the great pyramids of Giza.

tur.speed()

tur.fillcolor('orange')
tur.begin_fill()

i = 0
x = 25
while i < 33:
    tur.left(45)
    tur.forward(x)
    tur.right(90)
    tur.forward(x)
    tur.left(45)
    i = i + 11
    x = x*2
    tur.penup()
    tur.setposition(i*2,0)
    tur.pendown()

tur.setposition(0,0)
tur.end_fill()

tur.penup()
tur.setposition(-25,40)
tur.pendown()
tur.fillcolor('brown')
tur.begin_fill()
tur.circle(30)
tur.end_fill()

tur.penup()
tur.setposition(-25,45)
tur.pendown()

tur.fillcolor('yellow')
tur.begin_fill()
tur.circle(25)
tur.end_fill()
tur.left(90)
tur.forward(50)
tur.right(180)
tur.forward(25)
tur.right(90)
tur.forward(25)
tur.right(180)
tur.forward(50)
tur.right(180)
tur.forward(25)
tur.right(45)
tur.forward(25)
tur.right(180)
tur.forward(50)
tur.right(180)
tur.forward(25)
tur.right(90)
tur.forward(25)
tur.right(180)
tur.forward(50)

tur.penup()
tur.setposition(-30,55)
tur.pendown()

edge_length = 0
i = 0
while i < 10:
    tur.forward(edge_length)
    tur.right(154)
    i = i+1
    edge_length += 1

tur.penup()
tur.setposition(-31,75)
tur.pendown()

edge_length = 0
i = 0
while i < 10:
    tur.forward(edge_length)
    tur.right(154)
    i = i+1
    edge_length += 1

tur.penup()
tur.setposition(-23,80)
tur.pendown()

edge_length = 0
i = 0
while i < 10:
    tur.forward(edge_length)
    tur.right(154)
    i = i+1
    edge_length += 1

tur.penup()
tur.setposition(-15,57)
tur.pendown()

edge_length = 0
i = 0
while i < 10:
    tur.forward(edge_length)
    tur.right(154)
    i = i+1
    edge_length += 1

tur.penup()
tur.setposition(-13,71)
tur.pendown()

edge_length = 0
i = 0
while i < 10:
    tur.forward(edge_length)
    tur.right(154)
    i = i+1
    edge_length += 1

tur.penup()
tur.setposition(-36,67)
tur.pendown()

edge_length = 0
i = 0
while i < 10:
    tur.forward(edge_length)
    tur.right(154)
    i = i+1
    edge_length += 1

tur.done()
done()