'''
For each practice problem, write a function that returns a value (not just prints it). Y
ou can then call the function a couple times to test it, comment those calls out, 
and move on to the next problem. An example of this format is given below.


def func(x,y):
    return x + y

print(func(5,6))

'''

'''
Write a function that tells whether a number is even or odd 
(hint, compare a/2 and a//2, or use a%2)



def evenodd(a):
    if a % 2 == 0:
        return 'even'
    elif a % 2 != 0:
        return 'odd'

print(evenodd(5))



Write a function that returns True if a number within 10 of 100.



def eqtrue(x):
    if x >= 10 and x <= 100:
        return True
    else:
        return False

print(eqtrue(10))



Write a function that returns the maximum of 3 parameters.



def max3(a,b,c):
    return max(a,b,c)

print(max3(1,4,3))

Print out the powers of 2 from 2^0 to 2^20



def pow(a):
    for evalu in range(0,20):
        x = 2**(evalu)
        print(x)

print(pow(2))

'''
