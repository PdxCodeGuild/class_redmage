user_grade = float(input("what did you score on the test? "))

if user_grade >= 89.50:
    if  user_grade >=96.50:
        print("You received an A+! That's the highest possible letter grade! Wow! Nice job!")
    elif user_grade >=92.50:
        print("You received an A. That's really great work there! You only missed a couple points!")
    elif user_grade >=89.50:
        print("You received an A-. That's a really good score and you should be happy! Study and take your time to get that A or A+!")
elif user_grade >=79.50:
    if user_grade >= 86.50:
        print("You received a B+! Nice work. I believe you'll get an A next time!")
    elif user_grade >= 82.50:
        print("You received a B! That's above average for sure!")
    elif user_grade >= 79.50:
        print("You received a B-. That's still good but I think you can do better.")
elif user_grade >=69.50:
    if user_grade >= 76.50:
        print("You received a C+!")
    elif user_grade >= 72.50:
        print("You received a C!")
    elif user_grade >= 69.50:
        print("You received a C-.")
elif user_grade >=59.50:
    if user_grade >= 66.50:
        print("Well, it's a D+. That's below average. Come see me after class.")
    elif user_grade >= 62.50:
        print("Well that's a D!")
    elif user_grade >= 59.50:
        print("That's a D-.")
elif user_grade <59.49:
    print("You received an F on this test. That's a failing mark. Come see me after class.")
    pass