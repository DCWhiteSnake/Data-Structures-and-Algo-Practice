from timeit import timeit

testitem = '''
def factors(n):
    """High performance generator
    
    """
    x = 1
    while x <= n:
        while x*x < n:
            if n % x == 0:
                yield x
                x += 1
            else:
                x += 1
        x += 1 
        if x * x == n:
            yield x
        while x*x >n:
            if n % x == 0:
                yield x
                x += 1
            else:
                x +=1

p = []
for x in factors(100):
    p.append(x)
'''

print(timeit(stmt = testitem))

        
            

