import csv
# from easyfitness_app.models import Exercise

with open('fitness_scrape.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    for row in csv_reader:
        print(row)