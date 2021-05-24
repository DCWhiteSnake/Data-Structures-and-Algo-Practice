
def differentiate(expression):
    """ Function that finds the first differential of a polynomial expression
        
        expression         the polynomial expression

        if expression is a constant, the function returns 1.
        if expression is a number, the function returns 0.
        if the expressionis a polynomial expression the function returns the first differential.
    
    """

    is_number = False

    try:
        x = int(expression)                         # try to convert expression to a number, call this number x
        if isinstance(x, (int)):
            is_number = True # is is 
    except ValueError:
        is_number = False

    if len(expression) == 1 and is_number == False:
       
        return str(1)                                # The differential of a constant is one(1)

    elif is_number == True:
        return str(0)                                # The differential of a number is zero(0)

    else:
        number, constant, power = "", "",""          # Create string variables number, constant, and power to hold the similarly named variables.
        for x in range(len(expression)):
            try:               
                number += str(int(expression[x]))    # concatenate items in the expression to variable number until you meet an unparseable item
                                                     # store that item as constant i.e x, and record the positon
            except ValueError:
                position = x
                constant = expression[x]
                break
            
        for x in range(position+2, len(expression)): # add two to the location of the constant variable i.e., the positon of the exponent of the expression
                                                     # concatenate the remaining variables as power
                power += expression[x]
        
        number = int(number)
        try:
            power = int(power)                       # if power isn't given i.e in the case if 3x, assign a value of 1 to power
        except ValueError:
            power = 1
        if power != 1 :                             
            soln = str(number * power) + str(constant) + "^" + str(power-1)
        elif power == 1:                             # if power is  one, i.e., if we substract one from power it gives us zero,
                                                     # and x^0 is one, so we just return the number as solution
            soln = str(number)
        return soln


if __name__ == '__main__':
    user_input = input("Input the polynomial(s), seperate the operators by a single space")
    polynomial_eqn = user_input.split()
    soln = ""
    for x in range(len(polynomial_eqn)):
        if polynomial_eqn[x] in ['+', '-']:
            soln += str(polynomial_eqn[x]) + " "
        else:
            soln += differentiate(polynomial_eqn[x]) + " "
    print(soln)

    

    
