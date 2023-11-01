
#two types of decorators function and class
"""
function decorator is a func that takes a func as an argument and extends the behaviour of it without explicitly 
modifying it adding new functionality to existing func

In python functions are first class objects i.e they can be defined inside another function, 
passed as an argument to another function and can be returned from another function
"""

"""
uses:
timer decorator to calculate execution time of a function
debug decorator to print more info about the function and its arguments
check decorator to check arguments fulfill some requirements and depth behaviour
register functions like plug ins with decorators
cache return values
add information or update the state 
"""


def mydecorator(func):                      #decorator function takes a func as argument
    def printing():         
        print("Start printing")             #Extending functionality do something
        func()                              #perform some operation
        print("Stop printing")              #Extending functionality do something
    return printing

@mydecorator
def name():
    print("Suyash Agarwal")

name=mydecorator(name)                      #assigning name function as decorator function with name function as argument 
#the work of above line is done by decorator line @mydecorator
name()                                      #name function will gain new functionality 


#decorator with function having some arguments
import functools
def mydecorator(func):

    @functools.wraps(func)                  #to preserve identity of the function
    def calculate(*args,**kwargs):          #to accept any no. of arguments and keyword arguments *args and **kwargs is used
        print("Start calculating")
        result=func(*args,**kwargs)         #function also takes some arguments so also used here
        #if value is not stored in some variable then none as an output will be shown
        print("Stop calculating")
        return result
    return calculate

@mydecorator
def addx(x):
    return x+20

result=addx(10)                             #if returned value is not stored no result will be shown
print(result)
print(help(addx))
print(addx.__name__)


#decorator with some arguments
import functools
def repeat(num_times):                      #outer function
    def mydecorator(func):
        @functools.wraps(func)
        def inner(*args,**kwargs):
            for i in range(num_times):
                result=func(*args,**kwargs)
            return result
        return inner
    return mydecorator

@repeat(num_times=4)
def greet(name):
    print("Hello",name)

greet("Suyash")


#nested decorator executed in order they are listed
def decorator1(func):  
    def wrap():  
        print("$ $ $ $ $ $ $ $ $ $ $ $ $ $")  
        func()  
        print("$ $ $ $ $ $ $ $ $$ $ $ $ $")  
    return wrap  
  
def decorator2(func):  
  
    def wrap():  
        print("# # # # # # # # # # # # # #")  
        func()  
        print("# # # # # # # # # # # # # #")  
    return wrap  
 
@decorator1  
@decorator2  
def message():  
    print("Hello")  

message()


#class deorators same as function decorators but used if we want to maintain and update a state
class Count:

    def __init__(self,func):
        self.func=func
        self.num=0                          #create a state u want to store
    def __call__(self,*args,**kwargs):      #to implement class decorator call method is used
        self.num+=1                         #update state 
        print(f"This is executed {self.num} times")
        return self.func(*args,**kwargs)

@Count
def greet():
    print("Hello")

greet()
greet()
greet()