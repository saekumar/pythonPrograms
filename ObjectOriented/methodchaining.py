#method chaining: Calling multiple methods sequentially...each call performs an action on the same object and returns self

class Car:
    def start(self):
        print("YOU START THE ENGINE..") 
        return self
    def drive(self):
        print("YOU R DRIVING...")
        return self
    def stop(self):
        
        print("YOU STOPPED THE CAR..")
        return self

car=Car()
car.start()\
.drive()\
.stop()