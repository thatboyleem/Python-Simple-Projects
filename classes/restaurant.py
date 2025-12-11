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

new_res = Restaurant("the Famous", "interna continental")
new_res.describe_restaurant()
new_res.open_restaurant()
print(f"the name of this restaurant is {new_res.res_name}")
