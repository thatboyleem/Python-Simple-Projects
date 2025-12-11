class Restaurant:
    """this is a class to model a restaurant"""
    def __init__(self, res_name, cuisine_type):

        self.res_name = res_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """this prints two pieces of information about the restaurant"""
        print(f"the name of this restaurant is: {self.res_name}\nCuisine type: {self.cuisine_type}")
    def open_restaurant(self):
        if self.res_name:
            print(f"the restaurant is open, welcome to {self.res_name}")
        else:
            print(f"restaurant is closed")
    def set_number_served(self, number):
        """this function lets you set the number of customers served"""
        self.number_served= number
    
    def increment_number_served(self, number):
        """this function lets you increment the number of customers served"""
        self.number_served += number

    def get_number_served(self):
        """simple function to see the number of customers that have been served"""
        print(f"Served {self.number_served} customers")
    
my_restaurant = Restaurant('saleem', 'african')
my_restaurant.describe_restaurant()
my_restaurant.get_number_served()

my_restaurant.number_served = 4
my_restaurant.get_number_served()

my_restaurant.set_number_served(3)
my_restaurant.get_number_served()

my_restaurant.increment_number_served(3)
my_restaurant.get_number_served()