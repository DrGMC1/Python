# This program demonstrates passing two string
# arguments to a function.10/13

def main():
    first_name = input('Enter your first name ITS 250 student: ')
    last_name = input('Enter your last name: ')
    print('Your name reversed is')
    reverse_name(first_name, last_name)

def reverse_name(first, last):
    print(last, first)

# Call the main function.
main()

def simpOp(x, y):  
    z = x + y  
    print(z)

simpOp (1,5)
