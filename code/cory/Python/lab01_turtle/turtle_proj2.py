from turtle import *
speed(0)
#start
forward(200)
right(180)
forward(400)
right(180)
forward(200)

#ball
forward(100)
edge_length = 20
n_sides = 10
i = 0
while i < n_sides:
	forward(edge_length/n_sides)
	left(360/n_sides)
	i = i + 1
right(180)
forward(100)


#pole
right(90)
forward(200)

#flag
for i in range(0, 5):
    forward(100)
    right(90)

#number in flag
forward(50)
right(90)
penup()
forward(20)
pendown()
forward(60)
right(90)
forward(20)
right(180)
forward(40)
right(180)
forward(20)
right(90)
forward(60)
left(135)
forward(20)
penup()
forward(500)
pendown()

done()

# <------------------------- I was trying to spell my name, not enough time.
# # Letter C
# left(45)
# right(90)
# edge_length = 100
# n_sides = 100
# i = 0
# while i < n_sides:
# 	forward(edge_length/n_sides)
# 	left(180/n_sides)
# 	i = i + 1

# # Letter O
# penup()
# forward(20)
# # left(90)
# # forward(100)
# pendown()
# edge_length = 100
# n_sides = 100
# i = 0
# while i < n_sides:
# 	forward(edge_length/n_sides)
# 	left(360/n_sides)
# 	i = i + 1

# penup()
# forward(40)

# done()