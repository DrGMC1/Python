# This program displays a random number
# in the range of 0 through 45000.
import random

def main0():
    # Get a random number(example on how to call the randit function).
    # arguments in parentheses tell the function to give an integer random nums in range 1-100
    # number returned assignet tot he variable 'number'
    
    number = random.randint(0, 10)
    # Display the number.
    print('The number for random.randint is: ', number)

# Call the main function.
main0()

#------------randrange-----------------

def main1():
    # Get a random number.
    #The function will return a randomly selected number from the sequence 
    #of values 0 up to, but not including, the ending limit
    
    number = random.randrange(100)
    # Display the number.
    print('The number is for random.randrange', number)

# Call the main function.
main1()

#------------random-----------------

def main2():
    # Get a random number. Returns a random floating point
    # in the range of 0.0 up to 1.0(not including 1.0)
    
    number = random.random()
    # Display the number.
    print('The number is for random.random', number)

# Call the main function.
main2()

#------------uniform-----------------

def main2():
    # Get a random number. allows you to specify the range of values to select from
    number = random.uniform(0.0, 100.0)
    # Display the number.
    print('The number is for random.uniform', number)

# Call the main function.
main2()


###------------getrandbits-----------------
##
##def main4():
##    # Get a random number.
##    number = random.getrandbits(8)
##    # Display the number.
##    print('The number is for random.getrandbits', number)
##
### Call the main function.
##main4()
##
##
###------------Tringular-----------------
##
##def main4():
##    # Get a random number.
##    number = random.triangular(10,20,30)
##    # Display the number.
##    print('The number is for random.triangular', number)
##
### Call the main function.
##main4()


###------------The Seed-----------------

import random

random.seed(10)
print("seed example 1:", random.randint(1, 100))

random.seed(10)
print("seed example 2:",random.randint(1, 100))
print("seed example 3:",random.randint(1, 100))
print("seed example 4:",random.randint(1, 100))
