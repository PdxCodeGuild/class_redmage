from bs4 import BeautifulSoup
import requests
import csv

# Source URL for bodybuilding.com
source = requests.get('https://www.bodybuilding.com/exercises/finder/?exercisetypeid=1&muscleid=1').text

# Initializing soup
soup = BeautifulSoup(source, 'lxml')

# Creating csv file to write to
csv_file = open('fitness_scrape.csv', 'w', newline='')

csv_writer = csv.writer(csv_file)
csv_writer.writerow([
    'wrk_name', 
    'wrk_type', 
    'wrk_muscle', 
    'wrk_equip', 
    'wrk_level', 
    'wrk_img_1', 
    'wrk_img_2', 
    'msl_group_img', 
    'instructions'
    ])


# List to contain all exercise links
ex_link = []

# Used to loop through each result row to extract links
for result_row in soup.find_all('div', class_='ExResult-row'):

    work_link = "https://www.bodybuilding.com"
    work_link += result_row.h3.a['href']
    ex_link.append(work_link)

# Used for each exercise, stripped from previous for loop
for link in ex_link:
    pass

'''
****************************************************************************************************************************************************************
'''

# Using just the first link to get all variables down, will switch to for loop
link = ex_link[0]

# Source URL for bodybuilding.com
source = requests.get(f'{link}').text

# Initializing soup
soup = BeautifulSoup(source, 'lxml')

'''
********************************************************************************
Main div all data derives from, added name of workout
********************************************************************************
'''

# Main container for workout data
wrk = soup.find('div', class_="MainCol__container")

# Workout name
wrk_name = wrk.find('h2', class_='ExHeading ExHeading--h2 ExDetail-h2').text.strip()
# print(wrk_name)

'''
********************************************************************************
Top container, contains type, muscle worked, equipment, and level
********************************************************************************
'''

# Top container, contains type, muscle worked, equipment, and level
wrk_list = wrk.find('ul', class_='bb-list--plain')
wrk_list = wrk_list.find_all('li')

# Type
wrk_type = wrk_list[0].a.text.strip()
# print(wrk_type)

# Muscle Worked
wrk_muscle = wrk_list[1].a.text.strip()
# print(wrk_muscle)

# Equipment Used
wrk_equip = wrk_list[2].a.text.strip()
# print(wrk_equip)

# Level
wrk_level = wrk_list[3].text.strip().split(':') 
wrk_level = wrk_level[1].strip() # Had to go deeper, no tags just plain text
# print(wrk_level)

'''
********************************************************************************
Workout images, has two images
********************************************************************************
'''

# Workout images, has two images
wrk_img_cont = wrk.find('div', class_="flexo-container flexo-around")

wrk_img = wrk_img_cont.find_all('img')

wrk_img_1 = wrk_img[0]['src']
# print(wrk_img_1)

wrk_img_2 = wrk_img[1]['src']
# print(wrk_img_2)

'''
********************************************************************************
Muscle group, has one image
********************************************************************************
'''

# Muscle group, has one image
msl_group_section = wrk.find('section', class_="ExDetail-section ExDetail-guide")

msl_group_img = msl_group_section.find('img')['src']
# print(msl_group_img)

'''
********************************************************************************
Instructions
********************************************************************************
'''

# Instructions container
inst_cont = wrk.find('section', class_="ExDetail-section ExDetail-guide")

inst_ol = inst_cont.find('ol')

inst_li = inst_ol.find_all('li')

instructions = ''
for i in range(len(inst_li)):
    instruction = f'{i+1}' + '.) ' + inst_li[i].text + '\n\n'
    instructions += instruction

# print(instructions)

# Writing all variables
csv_writer.writerow([wrk_name, wrk_type, wrk_muscle, wrk_equip, wrk_level, wrk_img_1, wrk_img_2, msl_group_img, instructions])

# Closing file
csv_file.close()