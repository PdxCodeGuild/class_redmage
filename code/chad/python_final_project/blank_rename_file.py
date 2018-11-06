import os, random

source = '/home/chad/Documents/git_hub/class_redmage/code/chad/python_final_project/doc_send/'
destination = '/home/chad/Documents/git_hub/class_redmage/code/chad/python_final_project/doc_send/'

for filename in os.listdir(source):
    print(filename)
    src = source + filename
    dst = destination + 'testblank' + str(random.randint(0,1000)) + '.pdf'
    os.rename(src,dst)

    
# for filename in os.listdir(src):
#     print(filename)


# print(os.listdir(src))
