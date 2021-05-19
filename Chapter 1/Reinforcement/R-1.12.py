import random
def davidChoice(x):
    return x[random.randrange(0, len(x), 1)]

print(davidChoice("Extraordinary"))