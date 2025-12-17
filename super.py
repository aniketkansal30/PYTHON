class Employe:
    def __init__(self,name,id):
        self.name=name
        self.id=id
class Programmer(Employe):
    def __init__(self,name,id,lang):
        super().__init__(name,id)
        self.lang=lang
Aniket=Employe("Aniket Kansal",16)
Kansal=Programmer("Aniket Kansal",16,"Java")
print(Kansal.name)
print(Kansal.id)
print(Kansal.lang)