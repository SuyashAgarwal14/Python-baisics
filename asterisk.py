a=4*3                                   #can be used as multiplication operator
print(a)


a=2**4                                  #used for exponent
print(a)


#can be used to create list,tuples or strings of repeated elements
zeros=[0]*10
print(zeros)
zeros=[0,1]*10
s="AB"*10


#used for args ans kwargs as keyword only arguments

def function(a,b,*args,**kwargs):
    print(a,b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(kwargs)
function(1,2,3,4,five=5,six=6)


def function(a,b,*,c):                  #every argument after * is keyword argument-inforcing only keywoed arguments
    print(a,b,c)
function(1,2,3,4,c=5)


#argument unpacking
def function(a,b,c):                    #number of arguments must be equal to number of elements in the list
    print(a,b,c)

list1=[0,1,2]                           #tuples can also be used
function(*list)


def function(a,b,c):
    print(a,b,c)

dict1={'a':1,'b':2,'c':3}               #number of parameters must match number of keys and keys name must be same as parameters names
function(**dict1)


#unpacking containers: used for unpacking lists, tuples or sets into single or multiple remaining elemets
list1=[4,6,8,1,9]
beg,*mid,end=list1                      #unpacking of elements is always done into lists whether the container is tuple,set or list
print(beg,mid,end)

#merge iterables into list
list1=[1,2,3,4,5]
tuple1=(6,7,8,9,10)                     #set can alspo be used 
merged=[*list,*tuple1]
print(merged)

#merging two dictionaries
dict1={'a':1,'b':2,'c':3}
dict2={'d':4,'e':5,'f':6}
merged={**dict1,**dict2}
print(merged)