class Animal:
    alive=True
    def eat(self):
        print(" Eating...")

    def sleep(self):
        print("Sleeping...")

class Rabbit(Animal):
    def run(self):
        print("Runnnig...")
class Fish(Animal):
    def swim(self):
        print("Swimming....")
class Hawk(Animal):
    def fly(self):
        print("Flying...")
rab=Rabbit()
fish=Fish()
hawk=Hawk()
rab.eat()
rab.run()
hawk.fly()
fish.swim()
