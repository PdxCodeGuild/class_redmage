from PIL import Image
img = Image.open("/home/chad/Documents/git_hub/class_redmage/code/chad/lab_16/lena.png") # must be in same folder
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]

        y = 0.299*r + 0.587*g + 0.114*b
        pixels[i, j] = (int(y), int(y),int(y))
img.show()