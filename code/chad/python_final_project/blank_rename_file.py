import os, random

source = '/Users/chadbean/Documents/Programing and Development/github/class_redmage/code/chad/python_final_project/doc_send/'
destination = '/Users/chadbean/Documents/Programing and Development/github/class_redmage/code/chad/python_final_project/doc_send/'
counter = 0
for filename in os.listdir(source):
    print(filename)
    src = source + filename
    dst = destination + 'testblank' + str(counter) + '.pdf'
    os.rename(src,dst)
    counter += 1
print(counter)
    
# for filename in os.listdir(src):
#     print(filename)


# print(os.listdir(src))
