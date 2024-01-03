class Animal:
    def walk(self):
        print("walking!")


class Dog(Animal):
    def walk(self):
        print("dog walking")

class Cat(Animal):
    def speak(self):
        print("meow")

cat = Cat()
cat.speak()
cat.walk()

Dog().walk()