#Child class inherits from another child class...Also a child class can inherit from 2 different patent classes 
class Organism:
    alive=True
class Animal(Organism):
    def eat(self):
        print("Yeahhh....Iam eating....")

class dog(Animal):
    def bark(self):
        print("I will bark later...")

d=dog()
print(d.alive)
d.eat()
d.bark()