# Open FIle, store file in vairable, return variable and close file
import datetime
def open_file_read():
    with open('lab_24/hayden_island_rain.txt', 'r') as raindata:
        rain_data = raindata.read().strip('\n').split('\n')
    raindata.close()
    #print(rain_data)
    return rain_data
    
# Parse data
def parse_data(data):
    #Pop Out THe first Few Lines Of Data That Isnt Data
    for i in range(6):
        print(data.pop(i))
    # parse each line split into list, used for first loop
    line_parse = []
    # parse element[0] and element[1] into a list of dictionaries
    final_parse = []
    #First Loop splits each line into a list
    for line in data:
       line_parse.append(line.split())
    #Second loop strips out element[0] and element[1] into a dictionary. I used a try except 
    #Because I couldnt figure out which lines were messing it up even though i popped the first lines of the file
    for element in line_parse:
        try:
            final_parse.append({element[0]:element[1]})
        except:
            pass
    for line in final_parse:
        line[0] = line[0].datetime.s
    

# 1. Open data file as read
rain_data = open_file_read()

#2. Parse Data
parse_data(rain_data)