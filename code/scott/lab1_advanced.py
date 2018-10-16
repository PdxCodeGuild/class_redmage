from turtle import *

pencolor("blue")
bgcolor("red")
speed(10)

i = 0

while i < 360:
    fd(1)
    rt(1)
    i = i + 1

lt(90)
fd(100)
rt(90)
fd(200)
rt(90)
fd(400)
rt(90)
fd(400)
rt(90)
fd(400)
rt(90)
fd(200)
lt(45)
fd(100)
lt(135)
fd(142)
lt(135)
fd(100)
rt(45)
fd(100)
lt(18)

i = 1

while i < 6:
    fd(100)
    rt(144)
    i = i + 1

penup()


end_fill
done()
