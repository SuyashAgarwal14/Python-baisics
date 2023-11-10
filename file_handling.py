#to check for readability   .readable()
#append mode whe we write it writes at the end of file while in write mode it overrides the file  .write() to add text


#to delete file
#impport os     os.remove("filename")
#os.rmdir("filename")                   #to delete a folder


f=open(r'E:\Programs\Python\basics\file_handling_text.txt','r')          #default mode is reading else specify  r=read,w=write,a=append,r+=read and write
fname=f.name                                                             #give file name
mod=f.mode                                                               #gives mode of file
line=f.readline()                                                        #reads single line at a time and moves cursor to other line
contents=f.read()                                                        #to read file
contents=f.read(100)                                                     #to read file upto some size number of characters when written again read next 
contents=f.readlines()                                                   #gives a list with each line as an element
f.close()

#better to use context manager because they close the file as sson as we are out of it automatically as well as when encounter exceptions
with open(r'E:\Programs\Python\basics\file_handling_text.txt','r') as f:    
    
    #to read large data, iterate through every line thus manages memory as only one line read at a time not whole data
    for line in f:
        print(line,end='')

with open(r'E:\Programs\Python\basics\file_handling_text.txt','r') as f:    
    
    size_to_read=100
    f_contents=f.read(size_to_read)
    #to read large data, upto some size at a time
    while len(f_contents)>0:
        print(f_contents,end='')
        f_contents=f.read(size_to_read)