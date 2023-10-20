#tupples are fixed length,immutable,takes less memory ,efficient iteration
coordinates=(4,5,6,4)
cor=coordinates
cor=coordinates[1]
coordinates2=[(1,2),(3,4),(5,6)]                    #list of tupples
cor=coordinates.count(4)                            #counts no of occurence of a value
cor=coordinates.index(4)                            #index of first occurence o a value

cor=tuple(coordinates2)                             #convert to tuple

fruits = ("apple", "banana", "cherry","grapes")
(green, yellow, red,white) = fruits                 #brackets can be aviided
var=green
var=yellow
var=red
(green, yellow, *red) = fruits
var=green
var=yellow
var=red

#to join two tuples use + operator
tupple1=coordinates[1:3]    #slicing
tupple2=coordinates[::1]    #step argument
del(tupple1)        #delete tuple