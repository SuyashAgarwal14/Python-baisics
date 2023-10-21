#Part of Collections

#used to create light weight object types
from collections import namedtuple
point=namedtuple("Point","x,y")             #Point is the class name, point is the object name and x,y are the fields
pt=point(1,-4)
a,b=pt.x,pt.y


#dictionary that remembers the order in which elements are inserted, used before python3.7 to remember the order
from collections import OrderedDict
dict={}
dict['a']=1
dict['c']=3
dict['b']=4
dict['d']=2


#counter,namedtuple,OrderedDict,defaultDict,Dequeue
from collections import Counter

#Counter stores elements as dict keys in their counts as dict values
A="abbaaabbbbccc"                           #any iterable can be used 
item=Counter(A)
value=item
value=item.items()
value=item.keys()
value=item.values()
value=item.most_common(1)[0][0]            #returns value in a list of tupple pair thus to access individual element we have to give two indicis
value=item.most_common(1)
value=item.most_common(2)
value=item.most_common(1)[0]
value=item.most_common(1)[0][1]
value=tuple(item.elements())               #used to get all the elements upto their counts in ordered manner 


#used to set a default value of a key whose value has not been set
from collections import defaultdict
dict=defaultdict(float)
dict['a']=1
dict['b']=3
value=dict['a']
value=dict['c']


#double ended queue in which insertion and deletion can be done from both ends
from collections import deque
d=deque()
d.append(1)
d.append(3)
d.appendleft(2)
d.pop()
d.popleft()
d.extend([9,7,5])
d.extendleft([6,4,8])
d.rotate(2)                                #rotates twice from right for left rotation use negative like -2
d.clear()