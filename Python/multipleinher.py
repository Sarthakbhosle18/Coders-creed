class grandfather():
    def walk(self):
        print("i can walk")

class father(grandfather):
    def run(self):
        print("i can run")

class child(father,grandfather):
    def swim(self):
        print("i can swim")

p1= father()
p1.run()
p1.walk()

c1 = child()
c1.walk()
c1.run()
c1.swim()

        