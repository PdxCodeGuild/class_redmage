from PIL import Image, ImageDraw

width = 500
height = 500

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)


# the origin (0, 0) is at the top-left corner
#white background
draw.rectangle(((0, 0), (width, height)), fill="white")

# draw a rectangle from x0, y0 to x1, y1
#draw.rectangle(((100, 100), (300, 300)), fill="black")

#body arms and legs
draw.line((250, 200, 250, 350), fill="black")
draw.line((250, 350, 125, height), fill="black")
draw.line((250, 350, 375, height), fill="black")
draw.line((100, 250, 400, 250), fill="black")

draw.rectangle(((225, 250), (275, 350)), fill="black")
#the head
circle_x = width/2
circle_y = height/4
circle_radius = 100
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='yellow', outline='black')
#the eyes
circle_x = 200
circle_y = 100
circle_radius = 10
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='black', outline='black')

circle_x = 300
circle_y = 100
circle_radius = 10
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='black', outline='black')
#the mouth
draw.arc([200,100,300,175],50, 135, fill="black")
)


img.show()