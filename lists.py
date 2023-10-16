 
cars=["BMW","Audi","Honda","Maruti"]

#index starts from 0 but negative indexing strats from last -1 will be index of last element
value=cars[-2]                                    #Honda
value=cars[0]                                     #BMW
value=cars[1:]                                    #will access elemnts from 1 till last
value=cars[1:3]                                   #specify range including lower bound only  


#lists functions
bikes=["TVS","Hundai","BMW","Suzuki","Yamaha"]

bikes.insert(1,"Royal Enfield")                   #insert element at specific position
cars.append("Ferarri")                            #append an element in the list at last index
cars.extend(bikes)                                #appends two lists 
cars.remove("Yamaha")
cars.pop()                                        #removes last element from the array
cars.index("BMW")                                 #gives index of given element
cars.count("Hundai")                              #count number of recurring elements
cars.sort()                                       #sort in ascending order changes in the current list
cars.sort(key=len)
cars.sort(reverse=True)                           #sort in reverse order
new=sorted(cars)                                  #creates a sorte new list
cars2=cars.copy()                                 #copy elements of a list to another
cars.clear()                                      #clears whole list
length=len(cars)                                  #prints length of list
rev=reversed(cars)                                #reverse any iterable  sequence
cars.reverse()                                    #reverse the list only


#list comprehension
#newlist = [expression for item in iterable if condition == True]
#co=list(variable_name or any other ds)         converts to list


data=[]
data.append([cars,bikes])
new2=data[::2]                                    #step indexing every second element
list1=[2,5,8,3,1,3,8]
for index,value in enumerate(list1):              #returns a sequence of (index,value) tuple
    print(index,value)

zipped=zip(cars,bikes)                            #pair together lists,tuples or sequences to create a list of tuple 

#Nested list comprehension
transport=[cars,bikes]
A=[vehicle for mode in transport for vehicle in mode]