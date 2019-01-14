from bs4 import BeautifulSoup
import requests
import csv

'''
********************************************************************************
Creating CSV File
********************************************************************************
'''

# Creating csv file to write to
csv_file = open('fitness_scrape.csv', 'w', newline='')

csv_writer = csv.writer(csv_file)
csv_writer.writerow([
    'wrk_name', 
    'rating_num',
    'rating_name',
    'wrk_type', 
    'wrk_muscle', 
    'wrk_equip', 
    'wrk_level', 
    'wrk_img_1', 
    'wrk_img_2', 
    'msl_group_img', 
    'instructions'
    ])

'''
********************************************************************************
Lists for easy URL manipulation, see "source" variable in "Main Loop"
********************************************************************************
'''

ex_type_list = [1, 2, 3]

muscle_id_list = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
    11, 12, 13, 14, 15, 17, 18
]

'''
********************************************************************************
Main Loop
********************************************************************************
'''

# Source URL for bodybuilding.com // 1 = Stren ; 2 = Card ; 3 = Stret
for ex_type in ex_type_list:
    for muscle_id in muscle_id_list:

        source = requests.get(f'https://www.bodybuilding.com/exercises/finder/?exercisetypeid={ex_type}&muscleid={muscle_id}').text

        # Initializing soup
        soup = BeautifulSoup(source, 'lxml')

        # List to contain all exercise links
        ex_link = []

        # Used to loop through each result row to extract links
        for result_row in soup.find_all('div', class_='ExResult-row'):

            work_link = "https://www.bodybuilding.com"
            work_link += result_row.h3.a['href']
            ex_link.append(work_link)

        # Used for each exercise, stripped from previous for loop
        for link in ex_link:

            # Source URL for bodybuilding.com
            source = requests.get(f'{link}').text

            # Initializing soup
            soup = BeautifulSoup(source, 'lxml')

            '''
            ********************************************************************Main div all data derives from, added name of workout
            ********************************************************************
            '''

            # Main container for workout data
            wrk = soup.find('div', class_="MainCol__container")

            # Workout name
            wrk_name = wrk.find('h2', class_='ExHeading ExHeading--h2 ExDetail-h2').text.strip()
            # print(wrk_name)

            '''
            ********************************************************************
            Container just for rating and rating name
            ********************************************************************
            '''

            # Contains rating
            rating_container = soup.find('div', class_="ExRating")

            # Number rating (ex. 9.2)
            rating_num = rating_container.find('div', class_="ExRating-badge").text
            rating_num = rating_num.strip()
            # print(rating_num)

            # Rating Name (ex. Excellent)
            rating_name = rating_container.find('div', class_="ExRating-description").text
            rating_name = rating_name.strip()
            # print(rating_name)

            '''
            ********************************************************************
            Top container. Contains type, muscle worked, equipment, and level
            ********************************************************************
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
            ********************************************************************
            Workout images, has two images
            ********************************************************************
            '''

            # Workout images, has two images
            wrk_img_cont = wrk.find('div', class_="flexo-container flexo-around")

            wrk_img = wrk_img_cont.find_all('img')

            wrk_img_1 = wrk_img[0]['src']
            # print(wrk_img_1)

            wrk_img_2 = wrk_img[1]['src']
            # print(wrk_img_2)

            '''
            ********************************************************************
            Muscle group, has one image
            ********************************************************************
            '''

            # Muscle group, has one image
            msl_group_section = wrk.find('section', class_="ExDetail-section ExDetail-guide")

            msl_group_img = msl_group_section.find('img')['src']
            # print(msl_group_img)

            '''
            ********************************************************************
            Instructions
            ********************************************************************
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
            try:
                csv_writer.writerow([
                    wrk_name, 
                    rating_num, 
                    rating_name, 
                    wrk_type, 
                    wrk_muscle, 
                    wrk_equip, 
                    wrk_level, 
                    wrk_img_1, 
                    wrk_img_2, 
                    msl_group_img, 
                    instructions
                    ])
            except UnicodeEncodeError:
                print(UnicodeEncodeError) # Had one error with characters, manually added to csv, "Bear Crawl Fire Feet".

            '''
            ********************************************************************
            Print statements for command line, used to debug errors
            "Exercise Type = Stretching ; Muscle Type = Abductors ; Number = 7"
            ********************************************************************
            '''

            print(f'Exercise Type = {wrk_type} ; Muscle Type = {wrk_muscle} ; Number = {int(ex_link.index(link)) + 1}')
            print()

# Closing file
csv_file.close()