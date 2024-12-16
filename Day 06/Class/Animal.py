from time import sleep

class Animal:
    def __init__(self, name:str, age:int, weight:float):
        self.name = name
        self.age = age
        self.weight = weight
    def make_sound(self):
        pass

class Dog(Animal):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
    def make_sound(self):
        print(f"{self.name} said: ", end="")
        for i in range(4):
            print("Woof", end=" ")
            sleep(.5)
        print("\n")

class Cat(Animal):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
    def make_sound(self):
        print(f"{self.name} said: ", end="")
        for i in range(4):
            print("Meow", end=" ")
            sleep(.5)
        print("\n")

if __name__ == "__main__":
    gato = Cat("João", 5, 10.2)
    cachorro = Dog("Irineu", 7, 30)
    gato.make_sound()
    cachorro.make_sound()