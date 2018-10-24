from turtle import *

# Head
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)

# Body
penup()
forward(50)
pendown()
right(90)
forward(100)

# Right Arm
penup()
right(180)
forward(70)
pendown()
left(90)
forward(50)
penup()
left(180)
forward(50)
pendown()

# Left Arm
forward(50)
right(180)
forward(50)
left(90)
forward(70)

# Right Leg
right(45)
forward(70)
right(180)
forward(70)

# Left Leg
right(135)
left(45)
forward(70)
left(180)
forward(70)

done()

