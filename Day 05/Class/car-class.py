from time import sleep

class Car():
    def __init__(self, brand:str, color:str, gas:float):
        self.brand = brand
        self.color = color
        self.gas = gas
        self.is_on = False
    def start(self):
        if self.is_on == False and self.gas > 0:
            self.is_on = True
            print("The car is starting")
            for i in range(1, 4):
                print("Vrum" + ". "*i, end="")
        elif self.is_on == True:
            print("Car already on")
        else:
            print("Out of gas")
    def stop(self):
        if self.is_on == True:
            print("\nShutting off the car")
            self.is_on = False



if __name__ == "__main__":
    vw_beetle = Car("Volkswagen", "Blue", 4)

    vw_beetle.start()
    vw_beetle.stop()