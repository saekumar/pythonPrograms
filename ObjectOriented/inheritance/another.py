class person:
    def __init__(self,name="",age=0):
        self.name=name
        self.age=age
    def __lt__(self,other):
        if(self.age<other.age):
            return True
        else:
            return False
    def dis(self):
        print(self.name,self.age)
p1=person("Raja",5)
p2=person("Rani",7)

p1.dis()
print(p1<p2)