from turtle import *

speed(1000)

i = 0
while i < 73:
    forward(5)
    left(5)
    i = i + 1

x = 0
penup()
setposition(30,80)
pendown()
while x < 40:
    forward(2)
    right(10)
    x += 1

penup()
setposition(-10,80)
pendown()
y = 0
while y < 40:
    forward(2)
    right(10)
    y += 1

penup()
setposition(-10,30)
pendown()

forward(20)
left(20)
forward(20)
left(20)
forward(20)
left(20)
forward(20)
left(20)
forward(20)
left(20)

done()