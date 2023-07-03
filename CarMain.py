#John Carlo Ablay
#BSCPE 1-5
#Car Class
#July 1, 2023
import emoji
import pyfiglet
  
result = pyfiglet.figlet_format("Car Class", font = "alligator").center(120)
print(result)
author_name = ("Programmed by: John Carlo R. Ablay | BS Computer Engineering 1-5")
author_name_center = author_name.center(120)
print("\u001b[33;1m",author_name_center, "\u001b[37;1m")


#import car
from Car import Car
#create an object
car1 = Car()

#Call the accelerate method five times.
#Get the current speed of the car after each call and display it.
print('\033[94m'"**ACCELERATE -- 5 times**")

car1.accelerate()
car1.get_speed()
print("\u001b[37;1m""[1]")
car1.showInfo()

car1.accelerate()
car1.get_speed()
print("[2]")
car1.showInfo()

car1.accelerate()
car1.get_speed()
print("[3]")
car1.showInfo()

car1.accelerate()
car1.get_speed()
print("[4]")
car1.showInfo()

car1.accelerate()
car1.get_speed()
print("[5]")
car1.showInfo()


#Calls the brake method five times.
#Get the current speed of the car after each call and display it.
print("\n\n'\033[94m'****BRAKE -- 5 times****")
car1.brake()
car1.get_speed()
print("\u001b[37;1m""[1]")
car1.showInfo()

car1.brake()
car1.get_speed()
print("[2]")
car1.showInfo()

car1.brake()
car1.get_speed()
print("[3]")
car1.showInfo()

car1.brake()
car1.get_speed()
print("[4]")
car1.showInfo()

car1.brake()
car1.get_speed()
print("[5]")
car1.showInfo()

print("\nThank you for using my program! Have a good day!")
print(emoji.emojize('Have a good day! :grinning_face:'))
print(emoji.emojize(':motorcycle:'))
print(emoji.emojize(':taxi:'))
print(emoji.emojize(':bus:'))