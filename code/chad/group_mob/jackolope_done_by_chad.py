import random
#Name Template for when Function reproduce gets called
name = 'zuriel'

#Start of with two Jackalope for Begining
jackalope_tracker = [
    {'name': 'adam', 'age': 0},
    {'name': 'eve', 'age': 0}
]
#Years counter for what year we are on after all itterations of Jacks have processed
years = 0

# How many Jackalopes were removed at age 10
poppedtracker = []

#Flag to quit when Jackalopes hit 1000
flag = True

#Function Gets Called If Jacks Are Old Enough To Give Birth Check to see if jackolope is old enough this year to reproduce
def reproduce(jack):
    if jack['age'] >= 4 and jack['age'] <= 8:
        return jackalope_tracker.append({'name': name+str(random.randint(0,100)),'age':0 })

#Check to see if jackolope is old enough this year to reproduce, if it is, age+1
#Age the jack passed from loop reguardless what age
def age(jack):
    jack['age'] = jack['age'] + 1
    return jack

#Pop out jacks that are 10 years old
def pop_jacks(jack, i):
    if jack['age'] == 10:
        poppedtracker.append(jackalope_tracker.pop(i))

#Loop flag runs true unless jackalope hits 1000
while flag:
    print(jackalope_tracker)
    #for each jack in jack_tracker send to function to see if they can reproduce and age by one year
    for i in range(len(jackalope_tracker)):
        if len(jackalope_tracker) == 1000:
            print('You Have Reached 1000 Jacks')
            flag = False
            break
        age(jackalope_tracker[i])
        reproduce(jackalope_tracker[i])
        pop_jacks(jackalope_tracker[i], i)
    years += 1

print(f'You have a total of {len(jackalope_tracker)} Jack Population at {years} Years')
print(f'you popped {len(poppedtracker)} jacks total')