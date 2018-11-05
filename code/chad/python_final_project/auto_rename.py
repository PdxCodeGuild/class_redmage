import os, datetime

print(f'You Are Working In A {os.name} EnVironment')

#Ask User To Set The Path Where PDFs Are Stored:
path_input = input('What Path Are The PDFs Stored That You Would Like To Rename? > ')

os.chdir(path_input)
print(os.listdir())
is