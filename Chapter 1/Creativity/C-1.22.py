## Program that returns the dot product of values
##     c = []
##     if the arrays are not of the same length
##         output "The arrays are not of the same length"      
##     If the arrays contain any thing that is not a number
##         Output "The array has to be homogenous"
##     Else
##         For each value in the arrays 
##         Perform a dot(scalar product) and append the value to c
def dotprod(a,b):
    c = []
    try:
        if len(a) != len(b):
            return "The arrays are not of the same length"
        else:
            for x in range(len(a)):
                c.append(int(a[x])*int(b[x]))
            return c
    except ValueError:
        return "The array must contain only integers"
print("Give me array a")
a = list(eval(input()))
print("Give me array b")
b = list(eval(input()))

print(dotprod(a,b))