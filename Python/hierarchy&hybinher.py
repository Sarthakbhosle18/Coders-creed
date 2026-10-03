class Car:
    def name(self):
        print("audi")

class Color(Car):
    def colorname(self):
        print("red")

class Model(Car):
    def modelname(self):
        print("audi RS Q8")

class Engine(Color,Model):
    def motor(self):
        print("V6 engine")


# m = model()

c1 = Engine()
c1.name()
c1.colorname()
c1.modelname()
c1.motor()