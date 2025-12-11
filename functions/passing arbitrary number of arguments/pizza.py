def make_pizza(*toppings):#the asterisk in parameter name *toppings tells python to make a tuple called toppings
    """Print the list of toppings that have been requested"""
    print("\nMaking a pizza with the following toppings: ")
    for topping in toppings:
      print(f"-{topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')