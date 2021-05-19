x = [1,1,2,3,4]
try:
    x[54] = "Wonderful"
except IndexError:
    print("Don't try buffer overflow attacks in Python")