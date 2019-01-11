# Cory Morrissey's Capstone - 1/10/2019

### Project Name :
- "Easy Fitness"

### Project Overview :
- To create a mobile friendly workout instructor/tracker that allows users to easily create and combine workout routines. It is meant for people new to gyms or who have been working out for years, allowing everyone to get in and get out without worrying about all the planning. I will be using a Python library called "Beautiful Soup" to pull data from bodybuilding.com, and provide a structure for Cardio, Strength, and Stretching.

### Functionality :

- The initial homepage will have three options: Cardio, Strength, and Stretching(__/home/__). Once one of those are clicked, it offers a "templated" version that I will hard code in, and a "Build your own Workout" link that the user can follow to create a new workout (__/default/cardio/__). The templated version will have three options, as specified before. Each option will load a page that shows Day 1 - 3, and each day link will link to that days worth of workouts (__/default/cardio/day_1/__). 
- For the user created workout, the links will be similar up to when they click on which workout they would like to focus on (__/<username>/new/workout_1/__). If Strength is chosen, the user will have Day 1-3 links to click (__/<username>/new/workout_1/strength/day_1/__). At the top of each Day, there will be recommended muscle groups to work on. They will be limited to 10 workouts per day. Once they reach the limit, or decide enough workouts have been selected, there will be a save button at the bottom to save this workout as __"workout_1"__.

### Data Model :

- The data I will need to store will be 20 exercises for 16 muscle groups, for 3 different workout types. So 320 exercises times 3. So something like:

class Strength(models.Model):
    Chest
    Forearms
    Lats
    Middle Back
    Lower Back
    ...
    
class Cardio(models.Model):
    Chest
    Forearms
    Lats
    Middle Back
    Lower Back
    ...
    
### Schdeule :
- Data Scrape from bodybuilding.com, 2 days.
- Create website structure, template for default workouts 5 days (I will consider a static website finished for the sake of time, although very incomplete).
- Add user login, ability for users to register and create their own workouts (7 days).