#context managers allocates and free resources according to our need

#no need of try it will close the file even if there is exception
with open("E:\\Programs\\Python\\basics\\context_notes.txt",'w') as file:
    file.write("Hey, this is notes for context manager")                 
    

#for context manager of user defined class implement enter and exit method
class ManagedFile:
    def __init__(self,filename):
        print("init")
        self.filename=filename
    def __enter__(self):                                    #executed as soon as we enter with statement
        print("Enter")
        self.file=open(self.filename,'w')
        return self.file                                    #return allocated resource
    def __exit__(self,exc_type,exc_value,exc_traceback):
        if self.file:
            self.file.close()
        print("Exception:",exc_type,exc_value)              #None if no exception otherwise tells the type
        
        #to handle the raised exception if any
        if exc_type is not None:
            print("Exception is handled")
        print("exit")
        return True

with ManagedFile("E:\\Programs\\Python\\basics\\context_notes.txt") as file:
    print("doing something")
    file.write("typing something")
    file.addsome()
print("Continuing")


#same thing can be implemented as a function done below

from contextlib import contextmanager                       #have to use it as a decorator

@contextmanager
#create a function as generator
def open_managed_file(filename):
    #contents of enter function
    f=open(filename,'w')
    try:
        yield f
    #contents of exit function
    finally:
        f.close()

with open_managed_file("E:\\Programs\\Python\\basics\\context_notes.txt") as f:
    f.write("Learning ")