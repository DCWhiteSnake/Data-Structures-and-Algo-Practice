import math

print("***Calculator Program***")
solution = None

while solution == None:
    number_one_loopController = True
    number_two_loopController = True
    operator_loopController = True
    while number_one_loopController == True:
        try:
            numberOne = int(input("Input the first number here: "))
            number_one_loopController = False
        except TypeError:
            print("Please input a valid number")
            number_one_loopController = True
    while operator_loopController == True:
            operator = str(input("Operation: "))
            operator_loopController = False
            if operator not in ( '+' or '-' or '*' or '/'):
                print("input a valid operator")
                operator_loopController = True
    while number_two_loopController == True:
        try:
            numberTwo = int(input("Input the second number here: "))
            number_two_loopController = False
        except TypeError:
            print("Please input a valid number")
            number_two_loopController = True
    
    if(operator == '+'):
        solution = numberOne + numberTwo
    
    if(operator == '-'):
        solution = numberOne - numberTwo

    if(operator == '*'):
        solution = numberOne * numberTwo

    if(operator == '/'):
        solution = numberOne/numberTwo



print(solution)
        
                
