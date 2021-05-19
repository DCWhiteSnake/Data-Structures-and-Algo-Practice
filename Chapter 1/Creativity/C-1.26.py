a = int(input("Input a"))
b = int(input("Input b"))
c = int(input("input c"))
def simpleeqnchecker(a,b,c):
    truthiness = []
    
    truthiness.append(True if (a + b == c) else False)
    truthiness.append(True if (a == b - c) else False)
    truthiness.append(True if (a * b == c) else False)
    
    return truthiness