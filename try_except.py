
try:
    n=10
    a=int(input("Enter a number: "))
    result=n/a
    print(result)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Enter valid number")
else:
    print("Everything is fine")         #executes if there is no exception
finally:
    print("Try except successfull")     #executes after try catch is executed

    
"""
x,y=-1,0
if x<0:
    raise Exception('x positive')       #can throw an exception if condition is true

assert(x>=0)
assert(y>0), "X should be positive"
"""

class LowValueError(Exception):
    pass
class HighValueError(Exception):
    def __init__(self,message,value):
        self.message=message
        self.value=value

def get(x):
    if x<0:
        raise LowValueError("Value is negative")
    elif x>20:
        raise HighValueError("Value is greater than 20",x)

try:
    get(22)
except LowValueError as l:
    print(l)
except HighValueError as h:
    print(h.message,h.value)