from PIL import Image

import colorsys

img = Image.open(r"C:\Users\jeffr\Documents\Projects\class_redmage\code\jeffrey\Lenna_(test_image).png")
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]

# This line is used for v1

        # y = int(0.299*r + 0.587*g + 0.114*b)        
        # # r = y
        # # b = y
        # # g = y

        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
        
# Changing the values in this region satisfies version 2.

        h +=0
        s +=0
        v /=5

        r, g, b = colorsys.hsv_to_rgb(h, s, v)

        # convert back to RGB
        r = int(r*255)
        g = int(g*255)
        b = int(b*255)


        pixels[i, j] = (r, g, b)


img.show()