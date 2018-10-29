from PIL import Image
img = Image.open(r"C:\Users\jeffr\Documents\Projects\class_redmage\code\jeffrey\Lenna_(test_image).png")
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]

#         y = int(0.299*r + 0.587*g + 0.114*b)        
#         r = y
#         b = y
#         g = y

#         pixels[i, j] = (r, g, b)

# img.show()

import colorsys

# colorsys uses colors in the range [0, 1]
h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)

# do some math on h, s, v

r, g, b = colorsys.hsv_to_rgb(h, s, v)

# convert back to [0, 255]

r = int(r*255)
g = int(g*255)
b = int(b*255)

img.show()