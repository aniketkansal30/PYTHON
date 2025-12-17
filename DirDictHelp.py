x=[1,2,3]
print(dir(x)) #saare methods fun. bta dega

class Person:
    def __init__(self,age,name):
        self.name=name
        self.age=age
p=Person("Aniket",20)
print(p.__dict__) #dictionary form krdega

help(Person) #yeh pure data k baare m bta degaa
