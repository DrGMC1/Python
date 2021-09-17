### intro to if and else
##a = 100
##b = 20
##if a < b:
##    print ("True => a is greater than b")
##else:
##    print("False => b is not greater than a")


### Testing strings   
##s1 = "This"
##s2 = "this is also an string"
##
##print (s1 == 'this')
##print (s1 != 'this')

# This program compares two strings.
# Get a password from the user.
password = input('Enter the password: ')

# Determine whether the correct password
# was entered.
if password == 'myfavoriteprofessor':
    print('This is the best Password ever and is accepted.')
else:
    print('Sorry, that is the wrong password.')

### Character codes for the strings 'Mary' and 'Mark'
##name1 = 'Mary'
##name2 = 'Mark'
##
##if name1 > name2:
##    print('Mary is greater than Mark')
##else:
##    print('Mary is not greater than Mark')
##
### This program determines whether a bank customer
### qualifies for a loan.
##
##min_salary = 3000  # The minimum annual salary
##min_years = 2         # The minimum years on the job
##
### Get the customer's annual salary.
##salary = float(input('Enter your annual salary: '))
##
### Get the number of years on the current job.
##years_on_job = int(input('Enter the number of ' +
##                         'years employed: '))
##
### Determine whether the customer qualifies.
##if salary >= min_salary:
##    if years_on_job >= min_years:
##        print('You qualify for the loan.')
##    else:
##        print('You must have been employed',
##              'for at least', min_years,
##              'years to qualify.')
##else:
##    print('You must earn at least $',min_salary,  'per year to qualify.')
##
