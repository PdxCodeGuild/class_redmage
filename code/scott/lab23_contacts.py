# lab23_contacts.py

with open('contacts.csv', 'r') as file:
    lines = file.read().splitlines()
lines = [line.split(",") for line in lines]
contacts = [ {lines[0][0]: lines[i][0], lines[0][1]: lines[i][1], lines[0][2]: lines[i][2]} for i in range(1, len(lines))]