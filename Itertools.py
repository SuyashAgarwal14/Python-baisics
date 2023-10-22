
from itertools import product
#do the cartesian product of the two iterables
a=[1,2]
b=[3,4]
pro=list(product(a,b))
a=[1,2]
b=[3]
pro=list(product(a,b,repeat=2))


from itertools import permutations
a=[1,2,3]
per=list(permutations(a))
per=list(permutations(a,2))                         #list of permutations of 2 elements


from itertools import combinations,combinations_with_replacement
a=[1,2,3,4]
comb=list(combinations(a,2))                        #size of each combination must be defined 
comb=list(combinations_with_replacement(a,2))       #this will contain repeated elements also



from itertools import accumulate                    #accumulate makes an iterator that accumulated sums or any binary function
import operator                                     #to use operator with accumulate
a=[1,2,3,4]
accu=list(accumulate(a,func=operator.mul))          #do multiplication at each point
accu=list(accumulate(a,func=max))                   #find max at each point


#groupby makes an iterator that return keys and groups from iterable
from itertools import groupby
a=[1,5,2,3,4]
obj=groupby(a,key=lambda x: x<3)
for key,value in obj:
    print(key,list(value))

person=[{"name":"Suyash","age":21},{"name":"Aryan","age":21},{"name":"Paarisha","age":20},{"name":"Ayan","age":19}]
ob=groupby(person,key=lambda x: x["age"])
for key,value in ob:
    print(key,list(value))


from itertools import count,cycle,repeat
for i in count(10):
    print(i)
    if i==20:                                       #if condition is not mentioned infinite loop
        break

#cycle is used to iterate through an iterable repeatdily