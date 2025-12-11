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

    def update_odometer(self,mileage):#we are updating the odometer value through a method
        """set the odometer reading to the given value. Rejecct the change to roll the odometer back"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cant roll back the odometer mileage")

    def increment_odometer(self, miles):
        """add the given amount to the odometer reading"""
        self.odometer_reading += miles

class electricCar(car):
    """represent aspects of a car specific to electric vehicles"""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

my_leaf = electricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())