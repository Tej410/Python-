class Pygram:
    def __init__(self,name):
        self.name = name

    def talk(self):
        print(f"Hi this is {self.name} talking!")

john = Pygram("john")
print(john.name)
john.talk()            
