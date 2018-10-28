import random, time

#Name Template for when Function reproduce gets called
name = 'zuriel'

#Start of with two Jackalope for Begining
jackalope_tracker = [
    {'name': 'adam', 'age': 0, 'infected': 0},
    {'name': 'eve', 'age': 0, 'infected': 0}
]
#Years counter for what year we are on after all itterations of Jacks have processed
years = 0

# How many Jackalopes were removed at age 10
poppedtracker = []

# How many Jackalopes were poped after 2 years of catching a disease
infectedtracker = []

#Flag to quit when Jackalopes hit 1000
flag = True


#Function Gets Called If Jacks Are Old Enough To Give Birth Check to see if jackolope is old enough this year to reproduce
def reproduce(jack):
    if jack['age'] >= 4 and jack['age'] <= 8:
        return jackalope_tracker.append({'name': name+str(random.randint(0,100)),'age':0, 'infected': 0})

#Check to see if jackolope is old enough this year to reproduce, if it is, age+1
#Age the jack passed from loop reguardless what age
def age(jack):
    jack['age'] = jack['age'] + 1
    return jack

#Pop out jacks that are 10 years old
def pop_jacks(jack, i):
    if jack['age'] == 10:
        poppedtracker.append(jackalope_tracker.pop(i))

#Jack Got a disease and dies 2 years after catching, 1 in 10 chance. If == 10 infected goes to 1
#next time jack is checked and == 1 it goes to 2, next time pop to infecetd list
def infecetd_disease(jack, i):
    #random number generator to use for getting infecetd or not
    is_isnot_infeceted = random.randint(0, 2)
    # Check If population is extinct

    if jack['infected'] >= 3:
        infectedtracker.append(jackalope_tracker.pop(i))
        #print('you had a infected jackolope')
        time.sleep(.2)
    #infect the Jackolope if the is_isnot_infected ==
    if is_isnot_infeceted == 1:
        jack['infected'] += 1

    elif jack['infected'] == 1 or jack['infected'] == 2:
        jack['infected'] += 1




#Loop flag runs true unless jackalope hits 1000
while flag:
    #for each jack in jack_tracker send to function to see if they can reproduce and age by one year
    for i in range(len(jackalope_tracker)):
        if len(jackalope_tracker) == 1000:
            print(f'You Have Reached {len(jackalope_tracker)} Jacks')
            flag = False
            break
        if len(jackalope_tracker) <= 3:
            if years > 4:
                print('Jackolopes have gone extinct')
                time.sleep(3)
        try:

            age(jackalope_tracker[i])
            reproduce(jackalope_tracker[i])
            pop_jacks(jackalope_tracker[i], i)
            infecetd_disease(jackalope_tracker[i], i)
        #jackolopes are going extinct before the loop can run again. catch error
        except IndexError:
            print(f'you are at index{i}, jack must have been infected/popped and same index called again which '
                  f'doesnt exist anymore, catch error and keep going ')
            print(jackalope_tracker)
            print('')
            time.sleep(3)


    years += 1
    print(years)

print(f'You have a total of {len(jackalope_tracker)} Jack Population at {years} Years')
print(f'you had {len(poppedtracker)} Jackolopes Die Of Old Age')
print(f'you had {len(infectedtracker)} infected Jackolopes total')
print(jackalope_tracker)
