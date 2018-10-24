#grader.py
end = 'y'
while end == 'y':
    list_grade = input("What grade did you get on your test?  >")
    list_grade = int(list_grade)

    if list_grade >= 90 and list_grade <=100:
        end_grade = "A"
    if list_grade >= 80 and list_grade <=89:
        end_grade = "B"
    if list_grade >= 70 and list_grade <=79:
        end_grade = "C"
    if list_grade >= 60 and list_grade <=69:
        end_grade = "D"
    if list_grade >= 0 and list_grade <=59:
        end_grade = "F"

    if list_grade == 100:
        plus_minus = "+"
    elif list_grade <=59:
        plus_minus = "-"
    elif list_grade % 10 >=7:
        plus_minus = "+"
    elif list_grade % 10 >=5:
        plus_minus = " "
    elif list_grade % 10 <=4:
        plus_minus = "-"
    else: 
        pass  
    print(f"You got an {end_grade + plus_minus}!")
    while end != 'y' or  end != 'n':
            # This loop will ensure you choose y or n
            print("You must choose either y or n to continue!")
            end = input("Would you like to continue grading? > (y/n)") 
            if end == 'y':
                break
            if end == 'n':
                print("Thank you" + ',' + "goodbye " + '!' )
                break