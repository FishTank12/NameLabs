'''
We are going to implement the FizzBuzz challenge In order to do so 
We have to understand the conditions we need to do the challenge

Conditions: 

we first print the numbers 1 to 50 
if one of the ranges of these numbers then they should match
the conditions below:


For numbers that are multiples of 3  print Fizz 
For numbers that are multiples of 5, print Buzz

For multiples of both 3 and 5, print "FizzBuzz

And for all of the other numbers, we print the number itself

Since these are all based on conditions we might use while or if statements

Here are the multiples of 3: 3,6,9,12,15,18,21,24,27,30,33,36,39,42
,45,48 
in the program it will make sure that it sees them as "fizz" 
instead of the actual number itself

multiples of 5: 5,10,15,20,25,30,35,40,45,50

multiples of 3 and 5: 15,30,45
'''

def fizzBuzzing ():
 i = 1  # Initialize i
 while i <= 50:  # Loop through numbers from 1 to 50
    if i % 3 == 0 and i % 5 == 0:  # Check if divisible by both 3 and 5
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)

    i += 1  # Increment i to move to the next number
    fizzBuzzing()
'''
We can also write the same code but with for loops 


for i in range(1, 51):  # Loop through numbers from 1 to 50
    if i % 3 == 0 and i % 5 == 0:  # Check if divisible by both 3 and 5
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)

'''