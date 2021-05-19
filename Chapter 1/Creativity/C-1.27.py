
    
import timeit
naivefactors_v1 = '''
def factors(n):
    results = []
    for k in range(1,n+1):
        if n%k == 0:
            results.append(k)
    return results
    
x = factors(100)
'''

naivefactors_v2 = '''
def factors(n): # original generator that computes factors
    results = []
    for k in range(1, n+1):
        if n%k == 0:
            yield k

x =[]
for k in factors(100):
    x.append(k)
'''

upgradeone= '''
def factors(n):         # generator that computes factors
    k = 1
    while k*k < n:      # while k < sqrt(n)
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    if k*k == n: # special case if n is perfect square
        yield k
x =[]
for k in factors(100):
    x.append(k)
    
    
'''
upgradetwo = '''
def factors(n):
    k = 1
    while k*k < n:
        if n % k == 0:
            yield k
        k += 1
    if k*k == n: # special case if n is perfect square
        yield k
    k=k-1
    while k>0:
        if n % k == 0:
            yield n // k
        k -= 1
x = []
for k in factors(100):
    x.append(k) 
'''




print(timeit.timeit(stmt= naivefactors_v1)) # 5.624351600000011
print(timeit.timeit(stmt= naivefactors_v2)) # 5.963329299999998
print(timeit.timeit(stmt= upgradeone))      # 2.4994762000000037
print(timeit.timeit(stmt= upgradetwo))      # 3.226392599999997

        
