from PIL import Image
img = Image.open(r"C:\Users\jeffr\Documents\Projects\class_redmage\code\jeffrey\Lenna_(test_image).png")
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]

        y = int(0.299*r + 0.587*g + 0.114*b)        
        r = y
        b = y
        g = y

        pixels[i, j] = (r, g, b)

img.show()
