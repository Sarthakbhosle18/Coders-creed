class grandfather:
    def move(self):
        print("movements")
        print("i can walk")

class father(grandfather):
    def move(self):
        print("i can run")

class child(grandfather):
    def move(self):
        print("i can swim")
        
        
a1 = grandfather()
b1 = father()
c1 = child()

for i in (a1,b1,c1):
    i.move()        
