from math import*                   #to import math library

#String functions
#string is ordered,immutable

a="Suyash Agarwal"
var=a.upper()                       #changing case of String    .lower
var=a.upper().isupper()             #combination of two string methods upper and isuuper(checks case of String)
var=len(a)                          #prints length of Sting
var=a[1]                            #acces index of a chracter in String
var=a.index("yash")                 #tells index of a chracter or a string in the given string
var=a.replace("yash","rabh")        #rplaces first string with second at all occurences
var=a.find("S")                     #to find index of particular chrac or substring
var='S' in a                        #to check the presence of a particular sting boolean 
var=a[2:5]                          #prints element from 2 to 5(not included)same can be done with lists
var=a[::2]                          #step indexing
var=a[::-1]                         #step indexing to reverse a string
var=a.strip()                       #removes whitespace from begning and end
var=a.split()                       #splits the string into list with each word as an element can use a delimiter 
var=a.startswith("yash")            #endswith
var=a.count('s')

#  "delimiter".join(lsit_name)      used to join a list of strings into a single string
#fstrings is used to format the strings  shown in another file
            

'''
difference between index and find
           index()	                                              find()
Returns an exception if substring is not found	    Returns -1 if substring is not found
This can be applied to strings, lists and tuples	This can only be applied to strings
'''

#playing with numbers

a=-10
var=str(a)                          #converts number into string
#if u want to use a number with a string message convert it to string(cannot concat int with string)

var=abs(a)                          #absolute vale of a number
var=pow(2,3)                        #(2**3) can also be used for exponent of a number
var=max(2,4)                        #maximum of two
var=round(3.3)                      #round off a nuumber 
var=floor(3.6)                      #convert to smallest whole number      ceil,sqrt
var=a//3                            #to ignore decimal points // is used    
b=complex(a)                        #convert to complex   10+0j