
def sumofsquares_less_than_n(n):
    sum = 0
    for t in range(n):
        sum += (t*t)
    return sum

print( sumofsquares_less_than_n(4))