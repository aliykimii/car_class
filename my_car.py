
from electric_car import ElectricCar
from car import Car

tesla = ElectricCar("Tesla","Model S", 2019)
# print(tesla.get_descriptive_name())
# tesla.update_odometer(500)
# tesla.increment_odometer(1000)
# tesla.odometer()       
# print(tesla.describe_battery())
tesla.refuel_tank()
print(tesla.battery.battery_size)
print(tesla.battery.get_range())

new_car = Car("Mercedes","GLA 200",2020)
# print(new_car.get_descriptive_name()) 
# new_car.update_odometer(500)
# new_car.increment_odometer(1000)
# new_car.odometer()
new_car.refuel_tank()