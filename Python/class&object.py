# OOPs

class Car:

    def __init__(self,name,color):
        self.name = name 
        self.color = color
        self.speed = 0
        self.isStarted = False
        print(f"I have a {self.color} {self.name}")

    def __str__(self):
        return "This is a car class"
    
    def startCar(self):
        if not self.isStarted:
            self.isStarted = True
            print(f'{self.name} Started')
    
    def increaseSpeed(self):
        if self.isStarted :
            self.speed += 10
            print(f"{self.name}'s speed is {self.speed} kmph.")
        else:
            print("Please Start the Car")
    
    def decreaseSpeed(self):
        if self.isStarted :
            self.speed -= 10
            if self.speed < 0:
                self.isStarted = False
                return 
            print(f"{self.name}'s speed is {self.speed} kmph.")
        else:
            print("Please Start the Car")

c1 = Car("BMW",'red')
print(c1)
c1.startCar()
c1.increaseSpeed()
c1.increaseSpeed()
c1.increaseSpeed()
c1.decreaseSpeed()
c1.decreaseSpeed()
c1.decreaseSpeed()
c1.decreaseSpeed()
c1.decreaseSpeed()


c2 = Car("audi","black")