class car:
    """a simple attempt to represent a car"""
    def __init__(self, make, model, year):
        """initialize attributes to describe a car"""
        self.make= make
        self.model = model
        self.year = year
        self.odometer_reading= 0



    def get_descriptive_name(self):
        """return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model} "
        return long_name.title()
    def read_odometer(self):
        """Print a statement showing the cars mileage"""
        print(F"This car has {self.odometer_reading} miles on it")
class Battery:
    """a simple attempt to model a battery for an electric car"""
    def __init__(self, battery_size=40):
        """initialize the battery's attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}-kwh battery.")
    def get_range(self):
        """print a statement about the range this battery provides"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")
    def upgrade_battery(self):
        """check the battery size and upgrade it if necessary"""
        if self.battery_size != 65:
            self.battery_size = 65
            print("Battery upgraded to 65 kWh.")
        else:
            print("Battery is already at maximum capacity.")
class electricCar(car):
    """represent aspects of a car specific to electric vehicles"""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery= Battery()

    def describe_battery(self):
        """print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}-kwh battery.")

    
#my_new_car = car('audi', 'a4', 2024)
#print(my_new_car.get_descriptive_name())

#my_new_car.odometer_reading = 23 #modifying the odometer reading value
#my_new_car.read_odometer()