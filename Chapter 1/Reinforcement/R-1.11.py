# Imagine this :
# x = []
# for k in range(1,n+1):
#    x.append(k)
# Being shortened to this;
# List comprehension syntax typically go like this 
#  x = [ k for k in range(1, n+1) ]
# which assigns to x the list 1,2,3,..., n
# a more complex version of the list comprehension syntax is shown below
# x = [k for k in range(1,n+1) if condition]
# Here a condition has to be met for k to be added to x.
# So back to the problem at hand 
# We are tasked with replicating 
# this list [1, 2, 4, 8, 16, 32, 64, 128, 256] with the list comprehension
# syntax, basically anything raised to the power of 0 is 1, since we are 
# dealing mostly in powers of 2 we use the 'pow' function to get the necessary values,
# also the range function helps us to automatically increase the powers of 2 i.e as t, for us
x = [pow(2,t) for t in  range(0,9)] 
print(x)


