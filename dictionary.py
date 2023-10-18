monthconversion={
    1:"January",
    2:"February",
    3:"March",
    4:"April",
    "Jun":"June",
}
value=monthconversion[1]
value=monthconversion.get(2)
value=monthconversion.get(5)
print(monthconversion.get(5,"Invalid choice"))
print(monthconversion.get(5),"Invalid choice")
monthconversion[5]="May"
thisdict = dict(name = "John", age = 36, country = "Norway")    #to convert to or create a dictionary
x=monthconversion.keys()                                        #returns list of all the keys gets updated everytime you add new value to dict
y=monthconversion.values()                                      #returns list of all the values gets updated everytime you add new value to dict
z=monthconversion.items()                                       #Get a list of the key:value pairs as tuples
monthconversion.update({4:"July"})                              #to update a value also use to add new item

# pop() to delete a item   clear() to delete whole dictionary
#.pop() is used to delete the key,value pair and store value in another variable
del monthconversion["Jun"]                                      
month=dict(monthconversion)                                     #.copy() is also used to copy a dictionary

#Access items in list
for key,value in month.items():
    print(key,value)

