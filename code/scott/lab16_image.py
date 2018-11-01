# lab16_image.py

# import colorsys


# from PIL import Image
# img = Image.open("lenna.png")  # must be in same folder
# width, height = img.size
# pixels = img.load()

# for i in range(width):
#     for j in range(height):
#         r, g, b = pixels[i, j]

#         # Y = 0.299*r + 0.587*g + 0.114*b
#         # Y = int(Y)
#         # pixels[i, j] = Y, Y, Y

#         h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)

#         s = 1.5

#         r, g, b = colorsys.hsv_to_rgb(h, s, v)

#         r = int(r*255)
#         g = int(g*255)
#         b = int(b*255)

#         pixels[i, j] = r, g, b



# img.show()


from PIL import Image, ImageDraw

width = 500
height = 500

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)

draw.rectangle(((0, 0), (width, height)), fill="white")

# draw a rectangle from x0, y0 to x1, y1
draw.rectangle(((100, 150), (200, 300)), fill="lightblue")

# draw a line from x0, y0, x1, y1
# using the color pink
color = (256, 128, 128)  # pink
draw.line((100, 160, 25, 250), fill=color) # left arm
draw.line((200, 160, 275, 250), fill=color) # right arm

draw.line((110, 300, 90, 400), fill=color) # left leg
draw.line((190, 300, 210, 400), fill=color) # right leg

circle_x = 150
circle_y = 100
circle_radius = 50
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius,
              circle_x+circle_radius, circle_y+circle_radius), fill='lightgreen')

img.show()
