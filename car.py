class Car():
    """an attempt to model a car"""
    def __init__(self,make,model,year):
        """attributes of the car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """describes the full name of the car"""
        return f"{self.year} {self.make} {self.model}"

    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll the odometer backwards!")   

    def increment_odometer(self,miles):
        '''increases the value of odometer'''    
        self.odometer_reading += miles     

    def odometer(self):
        """prints out the odometer reading"""   
        print(f"This car has travelled {self.odometer_reading} miles.") 

    def refuel_tank(self):
        print(f"{self.make} is currently refueling...")    


   

        