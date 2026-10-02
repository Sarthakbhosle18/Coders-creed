class student:
    def name(self):
        print("my name is suresh")

class child(student):
    def age(self):
        print("im 20 year old")

class standerd(child):
    def std(self):
        print("im 10std")
    
c1=standerd()
c1.name()
c1.age()
c1.std()