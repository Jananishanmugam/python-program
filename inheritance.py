class a:
    def __init__(self):
        self.name = "Rahul"
    
    def display(self):
        print("a")
        return self.name

class b(a):
    def __init__(self):
        self.name = "Danny"
        super().__init__()
    
    def display(self):
        print("b")
        return self.name

class c(b,a):
    def __init__(self):
        super().__init__()
        
        
obj = c()
# print(obj.display())


class Parent():
    x = 1

class Child1(Parent):
    pass

class Child2(Parent):
    pass

print(Parent.x,Child1.x,Child2.x)

Child1.x = 2
print(Parent.x,Child1.x,Child2.x)

Parent.x = 3
print(Parent.x,Child1.x,Child2.x)  #this happens because initially child1 did not have that variable, now we have set the variable a value so, child1 initializes that variable value
#child1 remains 2

#changing both child1 and child2
Child1.x = 5
Child2.x = 6
print(Parent.x,Child1.x,Child2.x)


