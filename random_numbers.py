"""
random module for 
pseudo random numbers, called so because numbers are reproducible though seem random
secrets module for cryptographically strong numbers 
NumPy random to generate arrays with random numbers
"""


#since reproducible not recommeded due to security
import random
a=random.random()                           #produce float from 0 to 1
a=random.uniform(1,10)                      #to give range 
a=random.randint(1,10)                      #to get integers including upper bound
a=random.randint(0,1)                       #it gives values of 0 and 1 in random order used for situations (coin flip) like Head tail
a=random.randrange(2,20)                    #excludes upper bound

a=random.normalvariate(0, 10)               #first arrgument mu and second sigma 
#used for stats,picks random value from distribution with mean mu and standard deviation sigma

#have some functions to work on sequence
list1=list("Suyash Agarwal")
list1=['Red','Black','Green']
a=random.choices(list1)

a=random.choices(list1,weights=[10,15,5],k=5)
#k specifies how many random value we want of get at a time
#weigths represents chances of occurence 10/30 chance that occurence will be Red

a=random.sample(list1,3)                    #to pick more elements all unique
random.shuffle(list1)                       #to shuffle list

#to reproduce same output seed method is used  for same seed value same output is produced evrytime
random.seed(1)
a=random.random()
a=random.randint(1,10)
random.seed(2)
a=random.random()
a=random.randint(2,20)
random.seed(1)
a=random.random()
a=random.randint(1,10)
random.seed(2)
a=random.random()
a=random.randint(2,20)


import secrets
#only has three functions used for passwords, security tokens, account authentication.Takes more time
a=secrets.randbelow(10)                     #random integer excluding uper bound
a=secrets.randbits(3)                       #random numbers that can be represented in 3 bits

list1=list("Suyash Agarwal")
a=secrets.choice(list1)                     #random choice not reproducible



#Numpy random generator uses different number generator than from Python standard library
import numpy as np
a=np.random.rand(3)                         #creates a 1D array of random numbers
a=np.random.rand(3,3)                       #creates a 3X3 array of random numbers

#random integers excluding upper bound
a=np.random.randint(1,10)                   #prints single element
a=np.random.randint(1,10,3)                 #prints 1D list of 3 elements
a=np.random.randint(1,10,(3,4))             #prints 3X4 matrix of random integers
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
np.random.shuffle(arr)                      #shuffles the array by row no changes are made in the column

#Numpy seed generator
np.random.seed(1)
a=np.random.rand(3)
np.random.seed(1)
a=np.random.rand(3)
