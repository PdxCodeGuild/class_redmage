from PIL import Image
img = Image.open('Lenna_(test_image).png')
width, height = img.size
pixels = img.load()

from PIL import Image
img = Image.open("Lenna_(test_image).png") # must be in same folder
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        #print(226)
        #print(125)
        #print(137)
        r=
        g=1
        b=1
        Y = 0.299*r + 0.587*g + 0.114*b
        # your code here

        pixels[i, j] = (r, g, b)

img.show()
