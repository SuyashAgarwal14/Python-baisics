
#while loop

i=1
while i<10 :
    print(i)
    i+=1
print("End of while")



#for loop

friends=["Aryan","Samarth","Saksahm","Shanu"]
for friend in friends:
    print(friend)

for index in range(10):
    print(index)             #0-9
for index in range(3,10):
    print(index)             #3-9



#if we specify a third value to range parameter it will be our increment value start,stop,step
for x in range(2, 30, 3):
  print(x)