
def minmax(x):
    bubblesort(x)    
    return (x[0], x[len(x)-1 ])

def bubblesort(x):
   is_sorted = False
   last_unsorted = len(x)-1
   
   while (not is_sorted):
       is_sorted = True;
      
       for k in range(len(x) -1 ):
           if(x[k] > x[k+1]):
               swap(x, k, k+1)
               is_sorted = False
    
   
def swap(q, x,y):
    temp = q[x]
    q[x] = q[y]
    q[y] = temp
  
# Test values
p= [30,-5,4,5,200000,3,3,353,6343]

minmax(p)
print(minmax(p))
