# Function from Step 1 to ask user for data and return data as a list
def user_data():
    user_data = []
    while True:
        ask_user = input('Give me a number to analyze or type "q" to stop data collection? > ')
        if ask_user == 'q':
            break
        try:
            user_data.append(int(ask_user))
        except:
            #Try and remove spaces and then try and add into list again
            ask_user.strip()
            user_data.append(ask_user)
    print(user_data)
    return user_data

#Fucntion to find peaks from data and return to Step 2
def find_data_peaks(data):
    index = 0
    track_peaks = []
    for i in data:
        if index == 0:
            index +=1
        elif index == len(data)-1:
            continue
        elif data[index] > data[index - 1] and data[index] > data[index + 1]:
            track_peaks.append(index)
            index += 1
        else:
            index +=1
    return track_peaks
        
#Fucntion to find valleys from data and return to Step 3
def find_data_valleys(data):
    index = 0
    track_valleys = []
    for i in data:
        if index == 0:
            index +=1
        elif index == len(data)-1:
            continue
        elif data[index] < data[index - 1] and data[index] < data[index + 1]:
            track_valleys.append(index)
            index += 1
        else:
            index +=1
    return track_valleys

#Graph Results and Return to Step 4 from peaks and valley parameters in steps 1 and 2
def graph(data,peak,valley):
    print(peak)
    print(valley)
    print(data)
    counter = 1
    graph_data = []
    for num in range(len(data)):
        #list index 
        if num not in peak and num not in valley:
            if data[num] > data[num-1]
            graph_data.append(counter+1)
            elif data[num] == 
            
        elif num in peak or num in valley:
            graph_data.append(counter)
    print(graph_data)


#Welcome Print Statemetn
print('This Program Will Analaze Input Numbers Given and Output Peaks and Valleys Of Your Data')

#1. Call function to get data from user and put into a list and return into list variable
got_user_data = user_data()

#2. Call a function to find the peaks of the data
found_data_peaks = find_data_peaks(got_user_data)
#Print What the Peaks Indexes Are
print(f'You Found Peak At Index Positions {found_data_peaks} In Your Data List')

#3. Call a function to find the valleys of the data
found_data_valleys = find_data_valleys(got_user_data)
#Print What the Valley Indexes Are
print(f'You Found Valleys At Index Positions {found_data_valleys} In Your Data List')

#4. Call Function To Graph Your Results
graph(got_user_data, found_data_peaks, found_data_valleys)