add=lambda x:x+10
value=add(10)
mul=lambda x,y:x*y
value=mul(3,5)
l1=[(1,9),(2,8),(3,6),(4,7)]
sort=sorted(l1,key=lambda x: x[1])

#map function transforms each element with a function  map(func,sequence)
l2=[1,2,3,4]
m=map(lambda x: x*2,l2)                 #use list comprehension instead 
l3=[x*2 for x in l2]

#filter function gets a fuc and a seq.The func returns true or false and filter func returns elements for which func returns true
l4=filter(lambda x: x%2==0,l2)

#reduce function takes func and seq and repeatdily applies func to elements and return single value,The func has two arguments 
from functools import reduce
l4=reduce(lambda x,y:x*y,l2)
