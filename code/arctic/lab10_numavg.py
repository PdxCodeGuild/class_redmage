#numberaverage.py
#list the numbers
print("Welcome, this program will find the average of a list of numbers you enter. Type 'done' stop adding numbers.")

num_list = []
stop = ''
while stop != "done":
    user_choice = input(" ")
    if user_choice == "done":
        print("Thank you" + ', ' + 'Have a nice day' + '! ')
        break
    num_list.append (int(user_choice))
    print(num_list)

    # sum will add all elements in "num_list"
    sum(num_list)
    # len will determine the number of elements in "num_list"
    len(num_list)
    # avg = sum / len 
    # float = a decimal to the avg if needed
    # average = sum / len(num_list)
    avg = float(sum(num_list))/len(num_list)
    print(avg)