from PIL import Image, ImageDraw

width = 500
height = 500

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)

# the origin (0, 0) is at the top-left corner
draw.rectangle(((0, 0), (width, height)), fill='black')

# draw a rectangle from x0, y0 to x1, y1
# draw.rectangle(((100, 100), (400, 400)), fill='lightblue', outline='white', width=10)

# draw a line from x0, y0, x1, y1
# draw a line from x0, y1, xy, y0
# using the color pink

# color = (255, 128, 128)
# draw.line((0,0, width, height), fill=color, width=10)
# draw.line((0, height, width, 0), fill=color, width=10)

# Head
head_x = width/2
head_y = height/4
circle_radius = 100
draw.ellipse((head_x-circle_radius, head_y-circle_radius, head_x+circle_radius, head_y+circle_radius), fill='white')

# Left Eye
left_eye_x = 200
left_eye_y = 100
circle_radius = 25
draw.ellipse((left_eye_x-circle_radius, left_eye_y-circle_radius, left_eye_x+circle_radius, left_eye_y+circle_radius), fill='white', outline='black', width=2)

# Left iris
left_iris_x = 200
left_iris_y = 100
circle_radius = 10
draw.ellipse((left_iris_x-circle_radius, left_iris_y-circle_radius, left_iris_x+circle_radius, left_iris_y+circle_radius), fill='black', outline='black', width=2)

# Right Eye
right_eye_x = 300
right_eye_y = 100
circle_radius = 25
draw.ellipse((right_eye_x-circle_radius, right_eye_y-circle_radius, right_eye_x+circle_radius, right_eye_y+circle_radius), fill='white', outline='black', width=2)

# right iris
right_iris_x = 300
right_iris_y = 100
circle_radius = 10
draw.ellipse((right_iris_x-circle_radius, right_iris_y-circle_radius, right_iris_x+circle_radius, right_iris_y+circle_radius), fill='black', outline='black', width=2)

# Mouth
mouth_x = 250
mouth_y = 175
circle_radius = 20
draw.ellipse((mouth_x-circle_radius, mouth_y-circle_radius, mouth_x+circle_radius, mouth_y+circle_radius), fill='white', outline='black', width=2)

# Body
color = 'white'
draw.line((250, 200, 250, 375), fill=color, width=10)

# Arms
color = 'white'
draw.line((250, 300, 125, 225), fill=color, width=10)
draw.line((250, 300, 375, 225), fill=color, width=10)

# Legs
color = 'white'
draw.line((250, 375, 125, 450), fill=color, width=10)
draw.line((250, 375, 375, 450), fill=color, width=10)

img.show()