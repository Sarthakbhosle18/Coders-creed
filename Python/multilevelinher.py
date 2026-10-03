class father():
    def cook(self):
        print("i can cook")

class mother(father):
    def drive(self):
        print("i can drive")

class child(mother):
    def swim(self):
        print("i can swim")

c1 = child()
c1.cook()
c1.drive()
c1.swim()