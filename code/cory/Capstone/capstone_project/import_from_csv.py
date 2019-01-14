import csv
import os
path = "C:/Users/coryd/projects/class_redmage/code/cory/Capstone/capstone_project/"
os.chdir(path)
from easyfitness_app.models import Exercise

with open('fitness_scrape.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for row in csv_reader:
        p = Exercise(
            workout_name=row["workout_name"],
            rating_number=row["rating_number"], 
            rating_name=row["rating_name"], 
            workout_type=row["workout_type"], 
            workout_muscle=row["workout_muscle"], 
            workout_equipment=row["workout_equipment"], 
            workout_level=row["workout_level"], 
            workout_img_1=row["workout_img_1"], 
            workout_img_2=row["workout_img_2"], 
            muscle_group_img=row["muscle_group_img"], 
            instructions=row["instructions"], 
        )

        p.save()
