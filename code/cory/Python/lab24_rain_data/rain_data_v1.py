import datetime


# Open the file, makes a list that splits by each new line (thanks Chad)
with open('swan_island_pump.rain.txt', 'r') as rain_data:
    output_data = rain_data.read().strip('\n').split('\n')
    rain_data.close()

# Main function
def date_data(list_split_by_newline):

    # Removes lines that dont have raw data
    list_split_by_newline.reverse()
    for i in range(
        len(list_split_by_newline) - 1, # start
        len(list_split_by_newline) - 12, # stop
        -1): # step
        list_split_by_newline.pop(i) # do this
    
    # Creating a list of lists of data based on '\n' that we stripped out while opening
    data_list = [[list_split_by_newline[i]] for i in range(len(list_split_by_newline))]
    '''
    First try below
    for i in range(len(list_split_by_newline)):
        data_list.append([list_split_by_newline[i]])
    '''
    # Joins each list to create string values, then splits up by spaces so we can remove them from the data
    for i in range(len(data_list)):
        data_list[i] = ''.join(data_list[i])    
        data_list[i] = data_list[i].split(' ')

    # Actively removes the space values
    for x in range(len(data_list)):
        for y in range(len(data_list[x]) - 1, 0, -1):
            if data_list[x][y] == '':
                data_list[x].pop(y)

    # Now, each list contains just the values we need for indexing. Index 0 is the date, index 1 is the total rainfall. We create the list of tuples for our final results.
    tup_list = [(data_list[i][0], data_list[i][1]) for i in range(len(data_list))]
    '''
    First try below
    # for x in range(len(data_list)):
    #     tup_list.append((data_list[x][0], data_list[x][1]))
    '''

    return tup_list

# Creates our final result using date_data function
final_result = date_data(output_data)

# print(final_result)

# Lets user ask for dates
print("\nType 'quit' to quit.")
while True:
    user_input = input("\nWhat day would you like to look up? ex. '02-NOV-2018' >  ").upper()

    for i in range(len(final_result)):
        if final_result[i][0] == user_input:
            print(f'On {final_result[i][0]} it rained a total of {float(final_result[i][1])*.01} inches.')
    
    if user_input == 'QUIT':
        print()
        break

# date = datetime.datetime.strptime(f'{user_input}', '%d-%b-%Y')
# print(date.year)   # 2016
# print(date.month)  # 3
# print(date.day)    # 25
# print(date)  # 2016-03-25 00:00:00
# print(date.strftime('%d-%b-%Y'))  # 25-Mar-2016