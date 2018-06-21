#!/usr/bin/env python

#what we covered 
#classes
#objects
#instance
#class variables
#class methods
#instance variables
#instance functions

class Cars:
    tyres = 4 #class variables which can be accesed directly Cars.tyres
    steering = 1
    breaks = 1
   
    def __init__(self, make, model, color):
        self.make = make  #instance variables lfirstly this needs to be instansiated ante hima = Cars("ford" , "mustang", "yellow")
        self.model = model #hima.model
        self.color = color
        self.air_bags = 2
        
    
    def start_car(self): #hima.start_car()
        print("car started")

    def stop_car(self): #instance methods which can be accessed by hima.stop_car()
        print("car stopped")

    def change_gear(self):
        print("gear changed")

    def blow_horn(self):
        print("boooooo")


    def go(): #class methods which can be accessed directly Cars.go()
        print("car in motion")




print(Cars.tyres)
krish = Cars("ford", "mustang", "red")
print(krish.color)
hima = Cars("ford", "mustang", "yellow")
print(hima.color)
krish.start_car()  
krish.go()
krish.blow_horn()
print(krish.air_bags)
krish.air_bags = 4
print(krish.air_bags)
#car1.stop_car()

