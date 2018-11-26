# Version 1
# nums = [5, 0, 8, 3, 4, 1, 6]
# total = 0
# for i in range(len(nums)):
#     total += + i
# length = len(nums)
# print(f"The total given was {total}, the length is {length}, and the average is {total / length}.")

# Version 2

import string
num_string = list(string.digits)
num_string = ''.join(num_string)
print(num_string)
nums = []
end = False

while end == False:
    permission = False
    while permission == False: # Keeps user in loop until num_input is valid
        
        num_input = input("Add a number, we will see what the average is when you are done! Type in 'done' to finish! > ")
       
        if num_input == 'done': # Breaks if user is done
                permission = True
                break
        for x in num_input: # Checks each character individually, catches letters and double digits (if I didn't it wouldn't recognise '11' since it's not defined in the num_string)
            if x not in num_string:
                print("It didn't like that, let's try that again.")
                break
        else:
            permission = True

    while num_input == 'done':
        if len(nums):
            print(f"\nThe total number of inputs was {len(nums)}. The average number was {sum(nums) / len(nums)}\n")
            end = True
            break

    nums.append(int(num_input))
    print(nums)



