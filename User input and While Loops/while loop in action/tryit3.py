sandwich_orders = ['fish sandwich', 'tuna sandwich','barbecue sandwich', 'peanut butter sandwich',]
finished_sandwiches = []


while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    print(f"Taking {finished_sandwich.title()} order")
    finished_sandwiches.append(finished_sandwich)
#print a message listing all sandwiches that were made
print("\n----Orders-------")
for sandwich in finished_sandwiches:
    print(F"I made your {sandwich.title()}")