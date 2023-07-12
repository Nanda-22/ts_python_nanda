#Creating a child class Bus that will inherit all of the variables and methods of the Vehicle class
class Vehicle:

    def __init__(self,name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

s=Vehicle("audi", 300, 15)
print(s.name,s.max_speed,s.mileage)
