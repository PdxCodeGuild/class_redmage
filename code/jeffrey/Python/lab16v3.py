from PIL import Image, ImageDraw

width = 500
height = 500

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)


# the origin (0, 0) is at the top-left corner

draw.rectangle(((0, 0), (width, height)), fill="white")

# draw a line from x0, y0, x1, y1
# using the color pink
color_pink = (256, 128, 128)  # pink
color_gunmetal = (44,53,57)
draw.line((50, 225, 400, 225), fill=color_pink, width=4)
draw.line((500, 300, 250, 250), fill=color_pink, width=4)
draw.line((0, 300, 250, 250), fill=color_gunmetal, width=4)

# draw a rectangle from x0, y0 to x1, y1
draw.rectangle(((300, 300), (200, 200)), fill="lightblue")



circle_x = width/2
circle_y = height/2-100
circle_radius = 66
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='purple')

img.show()

from PIL import Image, ImageDraw
from random import randint

width = 500
height = 500

img = Image.new('RGB', (width, height))
draw = ImageDraw.Draw(img)

for i in range(1000):
    x0 = randint(0, width)
    y0 = randint(0, height)
    x1 = randint(0, width)
    y1 = randint(0, height)
    line_width = randint(1, 40)
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    draw.line((x0, y0, x1, y1), fill=(red, green, blue), width=line_width)

# img.show()