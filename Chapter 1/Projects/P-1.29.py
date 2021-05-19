from timeit import timeit
item ='''
def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]
'''

def all_perms(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] +  perm[i:]
'''
for all permutations of the array except first element:
    for all spots in the permutation to put first element in
        yield that permutation with first element inserted in that spot
        
'''

for x in all_perms(['d', 'o', 'g', 'c', 'a', 't']):
    print(x)



##for x in all_perms(list("abcdef")):
##    print(x)
##print(timeit(stmt = item))
##element = list("Adobe")
##print(element[1:])





##def perm(a, k=0):
##    if k == len(a):
##        print(a)
##    else:
##        for i in range(k, len(a)):
##         a[k], a[i] = a[i] ,a[k]
##         perm(a, k+1)
##         a[k], a[i] = a[i], a[k]
##
##perm(["c", "a", "t", "d", "o", "g"])
