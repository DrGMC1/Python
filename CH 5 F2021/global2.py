# Create a global variable. (#5, 10-18)
# intents to assign a value to the global number variable
number = 10

def main():
# global key word to declare the number
    global number
    number = int(input('Enter a number: '))
    show_number()

def show_number():
    print('The number you entered is', number)

# Call the main function.
main()

