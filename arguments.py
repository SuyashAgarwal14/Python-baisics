
#arguments-values passed for parameters while calling a function
#parameters-variables that are defined or used inside paraenthesis while defining a function
def print_name(name):                   #name is parameter
    print(name)

print_name("Suyash")                    #Suyash is argument



#positional and functional arguments
def numbers(a,b,c,d=6):
#d is default argument its value can be changed by assigning different value while calling, must be at the end only
    print(a,b,c,d)

numbers(1,2,c=3)                        #a and b are positional arguments and c is keyword arguments
#with keyword arguments we can shuffle the order but not with positional arguments
#keywords arguments can not be written before positional arguments
numbers(b=1,c=2,a=3)
numbers(3,2,1)


#args takes any number of positional arguments and kwargs takes any number of keyword arguments
def parameters(a,b,*args,**kwargs): 
    print(a,b)
    for arg in args:                    #args is a tuple
        print(arg)
    for key in kwargs:                  #kwargs is a dictionary
        print(key,kwargs[key])

parameters(1,2,3,4,5,six=6,seven=7)



#inforce only keyword argument all parameter after * are keyword parameters
def accept(a,b,*,c,d):
    print(a,b,c,d)
accept(1,2,c=41,d=9)



#argument unpacking
def accept(a,b,c):
    print(a,b,c)
mylist=[1,2,30]                         #length of container must match length of argument list in functon
accept(*mylist)                         #works with both tuple and dict but

#with dictionary keyname, parameter name, length of dict and function parameter must be same
my_dict={'a':2,'b':5,'c':9}
accept(**my_dict)                       # ** is used to unpack dictionary 



#to access global variable inside a function global keyword is used

#call by object and call by object reference

#Rule 1: parameters passed in is a reference to the object but reference is passed by value
#Rule 2: Mutable objects like dict and lists can be changed within a method 
#        But,if reference is rebind within a method then outer reference will still point to unchanged original object

#immutable objects like integers or strings cannot be changed within a method
#but immutable objects contained in mutable objects can be reassigned within a method

def check(x,a_list):    
    a_list.append(4)                    #mutable objects can be changed
    a_list[0]=-100                      #immutable objects(integers) in mutable object(list) can be changed, value changed to -100
    x=5                                 #creates a local variable

var=10      
mylist=[1,2,3]
check(var,mylist)
print(var)                              #integer so cannot be changed
print(mylist)                           #global list is changed



#rebind the mutable object reference and no change in global variable, creates a local variable
def check(a_list):
    a_list=[200,100,50]
    a_list.append(4)    
    a_list[0]=-100      
    print(a_list)

mylist=[1,2,3]
check(mylist)
print(mylist)                           #global list is unchanged



def check(a_list):
    a_list+=[200,100,50]                #this will affect the list
    a_list=a_list+[200,10,50]          #this will not affect the list
    
mylist=[1,2,3]
check(mylist)
print(mylist)