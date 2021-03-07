#calculator in python


#Take input from the user to choose one operator to perform the calculation
choose_operator = input(' Enter plus operator ‘+’ to Add or'
                        ' Enter Subtraction operator ‘-‘ to subtract or '
                        'Enter Multiplication operator ‘*’ to multiply or '
                        'Enter Division Operator ‘ / ‘ to Divide values ')

#Take two inputs values from the user to use in calculation
value_1 = int(input('Enter First Number: '))
value_2 = int(input('Enter Second Number: '))

# This function perform addition
def plus(value_1,value_2):
    value = value_1 + value_2
    return value

#This function perform subtraction
def minus(value_1,value_2):
    value = value_1- value_2
    return value

#This function perform multiplication
def multiply(value_1,value_2):
    value = value_1 * value_2
    return value

#This function perform division
def division(value_1,value_2):
    value = value_1 / value_2
    return value

#This if elif statements first check which operator user choose then they print the whole statement by performing selected operators

if choose_operator == '+':
    print('The Output is: ', value_1 , ' + ' , value_2 , '='  , plus(value_1,value_2))

elif choose_operator == '-':
    print('The Output is: ', value_1 , '-' , value_2 , '=', minus(value_1,value_2))

elif choose_operator == '*':
    print('The Output is: ', value_1 , '*' , value_2 , '=' , multiply(value_1,value_2))

elif choose_operator == '/':
        print('The Output is: ',  value_1 , '/' , value_2 , '=' , division(value_1 , value_2))

else:
    print('Please Give true inputs')