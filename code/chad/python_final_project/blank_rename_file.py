import os, random

source = '/Users/chadbean/Documents/Programing and Development/github/class_redmage/code/chad/python_final_project/doc_send/'
destination = '/Users/chadbean/Documents/Programing and Development/github/class_redmage/code/chad/python_final_project/doc_receive/'

for filename in os.listdir(source):
    print(filename)
    src = source + filename
    dst = destination + 'testblank' + str(random.randint(0,1000)) + '.pdf'
    os.rename(src,dst)

    
# for filename in os.listdir(src):
#     print(filename)


# print(os.listdir(src))
