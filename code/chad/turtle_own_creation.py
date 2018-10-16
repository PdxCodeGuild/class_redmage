from turtle import *

speed(500)

i = 0
while i < 73:
    forward(5)
    left(5)
    i = i + 1

x = 0
penup()
setposition(30,80)
pendown()
fillcolor('black')
begin_fill()
while x < 40:
    forward(2)
    right(10)
    x += 1
end_fill()

penup()
setposition(-10,80)
pendown()
fillcolor('black')
begin_fill()
y = 0
while y < 40:
    forward(2)
    right(10)
    y += 1
end_fill()

penup()
setposition(-25,40)
pendown()

forward(20)
left(40)
forward(20)
left(40)
forward(20)
left(40)
forward(20)
left(40)
forward(20)
left(40)

penup()
setposition(0,0)
pendown()


right(215)
forward(100)
right(45)
forward(75)
right(180)
forward(75)
right(90)
forward(75)
right(180)
forward(75)
right(45)
forward(50)
right(45)
forward(50)
left(180)
forward(50)
right(90)
forward(50)


done()