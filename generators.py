"""
generators are functions that return an object that can be iterated.
They generate the item inside object only one at a time and only when we ask for it thus more memory efficient.
defined like function but with yield instead of return
"""

def mygenerator():
    yield 1
    yield 2
    yield 3

g=mygenerator()                     #creating generator object

#print generator
# for i in g:
#     print(i)
#object has reached the end

value=next(g)                       #generator object generates stop iteartion when it does not reach another yield statement
print(value)
print(g)
print(sum(g))                       #can use then as inputs to other functions to take iterables



def countdown(num):
    print("Starting")
    while num>0:
        yield num
        num-=1

cd=countdown(4)
print(next(cd))                     #after each statement when yield encounters it stops there and next execution is resumed after it
print(next(cd))
print(next(cd))


import sys
def add(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num+=1
    return nums

def mygenerator(n):
    num = 0
    while num < n:
        yield num
        num+=1

print(sum(mygenerator(10)))
print(sum(add(10)))
print(sys.getsizeof(mygenerator(1000000)))
print(sys.getsizeof(add(1000000)))



def fibonacci(limit):
    a,b=0,1
    while a < limit:
        yield a
        a,b=b,a+b

fibo=fibonacci(30)
for i in fibo:
    print(i)



#generator expressions- they are written same as list comprehensions with parenthesis instead of square bracket
import sys
mygenerator=(i for i in range(10000) if i%2==0)
#for i in mygenerator:
#    print(i)
print(list(mygenerator))
mylist=[i for i in range(10000) if i%2==0]
print(mylist)
print(sys.getsizeof(mygenerator))
print(sys.getsizeof(mylist))