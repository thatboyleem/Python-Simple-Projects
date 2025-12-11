prompt = "\Please enter your Preferred toppings: "
prompt += "\n (Please enter 'quit' to finish order): "

toppings= ""
while toppings != 'quit':
    toppings = input(prompt)
    if toppings != 'quit':
      print(f"\nWe'll add {toppings.title()} to your pizza!")