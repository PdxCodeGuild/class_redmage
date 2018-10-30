import csv

with open('contact_list.csv', 'a+') as file:
    lines = file.read().split('\n')
    file.write("\njeffrey,banana,violet")




