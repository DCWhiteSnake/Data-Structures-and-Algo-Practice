def shuffler(data):
    import random
    print(data)
    datalen = len(data)
    for i in range(datalen):
        rint = random.randint(0, datalen-1)
        temp = data[i]
        data[i] = data[rint]
        data[rint] = temp
    
    return data
x = [1,2,3,4,5,6]
shuffler(x)
print('After First Shuffle')
print(x)
# print('New X')
# print(x)
# print('Second Shuffle')
# define sub_shuffle that takes in two variables, data and indexlist
# 	Imports the random module
# 	Creates a variable index and assigns the value of a random variable btw the range 0 and length of index list minus one, ends inclusive
# 	Creates a variable rElement and assigns  the value of the the data list at a position of indexlist[index] 
# 	Pops the value of index from the indexlist list
# 	returns the value of rElement
# 
# defines a custom_shuffle method that takes in data as argument
# 	defines a variable indexes_of_data and assignes the values of the range method while passing in the length of data i.e from 0 to length of data
# 	returns using the list generation syntax the values of sub_shuffle(data, indexes_of_data) for the range of 0 to length of data

## def sub_shuffle(data, indexlist):
##     import random
##     index = random.randint(0, len(indexlist) - 1)
##     rElement = data[indexlist[index]]
##     indexlist.pop(index)
##     return rElement
## 
## def custom_shuffle(data):
##     indexes_of_data = range(len(data))
##     return [sub_shuffle(data,indexes_of_data) for e in range(len(data))]
# def sub_shuffle(data, indexlist): 
#     import random 
#     index = random.randint(0, len(indexlist)-1) 
#     rElement = data[indexlist[index]] 
#     indexlist.pop(index) 
#     return rElement 
#  
# def custome_shuffle(data): 
#     indexes_of_data = list(range(len(data)) )
#     return [sub_shuffle(data, indexes_of_data) for e in range(len(data))]
# y = custome_shuffle(x)
# print(y)