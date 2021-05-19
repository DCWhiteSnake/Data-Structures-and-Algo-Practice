"""Let's say we are given:
stop = 20
start = 5
step = 5

5 10 15 20
number of elements is 4

(20 - 5) = distance between the points
(5 - 1) = step minus 1
We do the true division so that we get a whole number estimate

"""

"""
Using (stop - start) // step = 8

stop = 21
start = 5
step = 2
 
5 7 9 11 13 15 17 19 21
Using (stop - start + step -1)// step
(21 - 5 + 2 -1 )//2 = 
"""
number_of_items = (50 - 13 )// 13
print(number_of_items)
