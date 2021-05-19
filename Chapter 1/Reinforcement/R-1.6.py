def oddsquaresum(x):
    sum = 0
    for p in range(1,x):
        if p % 2 == 1:
            sum += p*p
        else:
            pass
    return sum

print(oddsquaresum(5))


