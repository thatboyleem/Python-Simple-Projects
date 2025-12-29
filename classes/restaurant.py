class Restaurant:
    """this is a class to model a restaurant"""
    def __init__(self, res_name, cuisine_type):

        self.res_name = res_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """this prints two pieces of information about the restaurant"""
        print(f"the name of this restaurant is: {self.res_name}\nCuisine type: {self.cuisine_type}")
    def open_restaurant(self):
        if self.res_name:
            print(f"the restaurant is open, welcome to {self.res_name}")
        else:
            print(f"restaurant is closed")

class IceCreamStand(Restaurant):
    """this is a subclass of Restaurant to model an ice cream stand"""
    def __init__(self, res_name, cuisine_type='ice cream'):
        super().__init__(res_name, cuisine_type)
        self.flavors = ['chocolate', 'vanilla', 'strawberry']

    def display_flavors(self):
        """this method displays the flavors available"""
        print("the available flavors are:")
        for flavor in self.flavors:
            print(f"- {flavor}")

new_res = Restaurant("the Famous", "interna continental")
new_res.describe_restaurant()
new_res.open_restaurant()
print(f"the name of this restaurant is {new_res.res_name}")

Vanilla_ice_cream_stand = IceCreamStand("Sweet Treats")
Vanilla_ice_cream_stand.describe_restaurant()
Vanilla_ice_cream_stand.display_flavors()

