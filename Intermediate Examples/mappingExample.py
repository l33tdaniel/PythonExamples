#3 map function
'''
map() function, this function takes two arguments: a function and a list.
It then applies the function to all of the values of the list of and creates 
a new values with the returned values from the function.

'''



li = [1,2,3,4,5,6,7,8,9,10]

def function(x):
    return x**x


#seems to be a small problem with the code here.. might fix later
print((func(x) for x in li if x % 2==0))