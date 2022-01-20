from car import Car

class Battery():
    def __init__(self,battery_size = 75):
        """setting the atttributes of the battery"""
        self.battery_size = battery_size
        
    def describe_battery(self):
        """prints out the the size of the battery """
        print(f"This car has a {self.battery_size} kW battery.")

    def get_range(self):
        """prints out the range of the car can travel"""
        if self.battery_size == 75:
            range = 360
        if self.battery_size == 100:
            range = 480
        print(f"This car can  go {range} miles.")


class ElectricCar(Car):
    '''an attempt to model an electric car from an existing car'''
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()

    def refuel_tank(self):
        print(f"{self.make} doesn't have a fuel tank.") 