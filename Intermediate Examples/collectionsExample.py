import collections
from collections import Counter

'''
What is an immutable object? 
State can be changed if someting is a mutable object
mutable objects can change their state or contents and immutable objects
can't change their state or content

Immutable objects: int, float, bool, string, unicode, tuple
Mutable objects are list, dict, and set Custom classes are also generalyl mutable


'''
#Containers
#list
#set
#dict
#tuple - inmuttable

#Types 
#1 counter <- this video
#2 Deque
#e namedTuple()
#4 orderdDict
#5 defaultdict




c = Counter('gallad')
print(c)
c = Counter(['a', 'a','b', 'c', 'c'])
print(c)
c = Counter({'a':1, "b":2})















