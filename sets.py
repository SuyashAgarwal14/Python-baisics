#unordered,mutable and no duplicates
marks={98,99,100,99,97}                 #does not store duplicate values

#iterate through sets
for score in marks:
    print(score)

list1=[3,6,9,12]
set1=set(list1)                         #to convert into set

marks.add(100)
extra=[80,81]
marks.update(extra)                     #to add other collection elements to the set .unionalso can be used   
marks.remove(100)                       #to delete particular element can use discard also(discard does not give error if not present)
marks.clear()                           #delete marks
extras=set(extra)

#Return a set that contains the items that exist in both set x, and set y:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)                   #x&y is also used for intersection
x.intersection_update(y)
#Keep the items that are not present in both sets:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)        #it updates in the firt variable i.e x
z = x.symmetric_difference(y)           #it returns the set into a new variable 
q=x.difference(y)                       #different elements in x from y only while in above examples from both sets are considered

p=x.union(y)                            #to take union of both the sets  (x|y is also used for union)
x.issubset(y)                           #returns boolean value
x.issuperset(y)                         #boolean value
x.isdisjoint(y)                         #no common elements in both sets boolean value

#to copy a set
setP={1,2,3,4}
setQ=setP
setR=setP.copy()
setR=set(setP)  
setA=frozenset(setP)                    #only union,intersection and difference methods can be used fix the set ,can use any iterable