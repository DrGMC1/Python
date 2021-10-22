# This program demonstrates an argument being
# passed to a function. )10/13

def main():
    value = 5
    show_double(value)
    
# The show_double function accepts an argument
# and displays double its value.

def show_double(number):
    result = number * 4
    print(result)

# Call the main function.
#To call a function, use the function name followed by parenthesis
main()
