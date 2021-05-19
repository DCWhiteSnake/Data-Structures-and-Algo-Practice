
def norm(v,p = 2):
    y = 0
    if p == 2:
        for x in range(len(v)):
            y += v[x]**p
        return y ** (1/p) 
    if p>0 and p != 2:
        for x in range(len(v)):
            y += v[x] ** p
        return y ** (1/p)

