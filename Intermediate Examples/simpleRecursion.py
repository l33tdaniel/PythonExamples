'''
Factorial is one example of recursion
5! = 5*4*3*2*1
The below example assumes that the factorial number being tossed in is greater than 0

Recursion happens when a function calls itself

We want to avoid a stack overflow, and yes, that's what the website is named after. here's an example of what a stack overflow looks like in code

void ping()
{
  pong();
}

void pong()
{
ping();
}

it keeps calling itself, right?

Lets look at Fibonacci's sequence, which starts as 0,1,1,2,3,5,8,13,21

As we'll see, recursion is slower in this method, but it's not always slower
'''
import time

#This is doing it without recursion
def fibonacci(idx):
    seq = [0,1]
    for i in range(idx):
        seq.append(seq[-1]+seq[-2])
    return seq[-2]

#This is doing it with recursion
def Fibonacci(index_of_number):
    if index_of_number <= 1:
        return index_of_number
    else: 
        return Fibonacci(index_of_number-1)+Fibonacci(index_of_number-2)
print("****** recursion ******")
rec = time.time()
print(Fibonacci(37))
print("speed: " + str(time.time()-rec))
print("****** not recursion ******")
it = time.time()
print(fibonacci(37))
print("speed : " + str(time.time()-it))
 #Running this should give you 21, since 21 is the 8th index in the fibbonacci sequence







