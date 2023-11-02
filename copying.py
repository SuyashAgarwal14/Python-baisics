#copy mutable elements with a built in copy module

a=5
b=a                                         #it will not make a real copy rather new variable with same referrence both point to same number
b=6                                         #creates new variable
print(a,b)                                  #different values 


#when we copy an iterable, reference is copied thus .copy() is used but its shallow, to change at inner level deepcopy is used
mylist=[0,1,2,3,4]
cpylist=mylist
cpylist[0]=-10
print(mylist)
print(cpylist)                              #both have same values because assignment does not make actual copy


#to make actual copy use copy module.
#Shallow copy-one level deep copy,but then only references of nested child objects
#Deep copy-full independent copy

import copy
mylist=[0,1,2,3,4]

#with list shallow copy can be made by several ways
cpylist=copy.copy(mylist)       
cpylist=mylist.copy()
cpylist=list(mylist)
cpylist=mylist[:]
cpylist[0]=-10
print(mylist)
print(cpylist)


#deep copy is used to copy nested iterables(list, dictionary and tuples) while shallow for single iterable
import copy
mylist=[[0,1,2,3,4],[5,6,7,8,9]]
cpylist=copy.copy(mylist)                   #shallow copy only one level deep so does not work as it did for 1D iterable
cpylist[0][1]=-10
print(mylist)
print(cpylist)

mylist=[[0,1,2,3,4],[5,6,7,8,9]]
cpylist=copy.deepcopy(mylist)               #deep copy
cpylist[0][1]=-10
print(mylist)
print(cpylist)



#for custom objects

#shallow copy
import copy
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
p1=Person("Suyash",27)
p2=p1                                       #not an actual copy but reference copy
p2.age=28
p3=copy.copy(p1)
p3.age=20
print(p1.age)
print(p2.age)
print(p3.age)


#deep copy
import copy
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Employee:
    def __init__(self,boss,employee):
        self.boss=boss
        self.employee=employee
    
p1=Person("Suyash",57)
p2=Person("Manu",30)
company=Employee(p1,p2)
company_clone=copy.copy(company)        
company_clone.boss.age=60                   #original gets affected because of shallow copy in deeper content
print(company_clone.boss.age)
print(company.boss.age)

company_clone2=copy.deepcopy(company)
company_clone2.boss.age=60
print(company_clone2.boss.age)