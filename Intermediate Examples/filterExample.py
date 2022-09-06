#4 Filter Function

'''
filter() function, the filter function is very similar to the map() function shown in the previous video. 
It takes again, two arguments (function, iterable) and applies the function to all of the items in the iterable. 
If the function returns a True value then that item will be added to a new list.
'''

def add7(x):
    return x+7

def isOdd(x):
    return x%2 != 0

a = [1,2,3,4,5,6,7,8,9,10]

b = list(filter(isOdd,a))

c = list(map(add7,filter(isOdd,a)))

#  LAMBDA!!!