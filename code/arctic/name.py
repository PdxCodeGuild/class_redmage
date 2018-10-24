# JL name
from turtle import *

forward(45)
right(90)
forward(25)
right(90)
forward(25)
left(90)
forward(100)
right(90)

n_sides = 4
edge_length = 15

i = 0

while i < 6:
	forward(edge_length)
	right(5/n_sides)
	i = i + 1
	edge_length = edge_length + 1

n_sides = 4
edge_length = 6

i = 0

while i < 7:
	forward(edge_length)
	right(100/n_sides)
	i = i + 1
	edge_length = edge_length + 1

forward(85)
left(93)
forward(55)
left(90)
forward(25)
right(90)
forward(24)
right(90)
forward(35)

penup()
forward(100)
right(90)
pendown()
forward(125)
left(90)
forward(75)
left(90)
forward(25)
left(90)
forward(55)
right(90)
forward(100)
left(90)
forward(20)
penup()

done()
