class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def print_details(self):
        print(self.name,self.age)
class Student(Person):
    def __init__(self, name, age):
        print("Hello")
        super().__init__(name, age)     #class name can also be used instead of super
p=Student("Suyash",20)
p.print_details()