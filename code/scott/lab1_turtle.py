# lab1: Turtle

# importing all the tools from turtle
from turtle import *

#starting out
penup()
setposition(0, 300)
pendown()

fillcolor("blue")
begin_fill()

fd(50)
rt(90)
fd(50)
rt(90)
fd(50)
rt(90)
fd(50)

end_fill()

bk(50)
rt(90)
fd(25)
rt(90)
fd(25)
rt(90)

fillcolor("red")
begin_fill()

fd(50)
lt(90)
fd(150)
lt(90)
fd(100)
lt(90)
fd(150)
lt(90)
fd(100)

end_fill()

lt(45)
fd(150)
bk(150)
rt(225)
fd(100)
rt(45)
fd(150)
bk(150)
rt(45)
fd(150)
rt(90)
fd(25)
lt(120)
fd(200)
bk(200)
rt(120)
fd(50)
lt(60)
fd(200)



done()
