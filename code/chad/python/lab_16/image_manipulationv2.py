import colorsys
from PIL import Image
 # must be in same folder
img = Image.open("/home/chad/Documents/git_hub/class_redmage/code/chad/lab_16/lena.png")
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]

        # colorsys uses colors in the range [0, 1]
        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
        h *= 1.025
        s *= 1.5
        v *= 1
        # do some math on h, s, v

        r, g, b = colorsys.hsv_to_rgb(h, s, v)

        # convert back to [0, 255]

        r = int(r*255)
        g = int(g*255)
        b = int(b*255)
        #y = 0.299*r + 0.587*g + 0.114*b
        pixels[i, j] = r, g, b
       
img.show()



