#create a class car
class Car:
    #def init (model, brand, speed)
    def __init__ (self, model=2022, make="Chevrolet Trailblazer", speed=0):
        self.__year_model = model
        self.__make = make
        self.__speed = speed
    #accelerate
    def accelerate(self):
        self.__speed += 5

    #break
    def brake(self):
        self.__speed -= 5
    
    #get speed of the car
    def get_speed(self):
        return self.__speed

    #show info
    def showInfo(self):
        print("Speed:", self.__speed)