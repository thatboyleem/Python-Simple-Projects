#here we'll be modifying a list, any changes made to a list are permanent
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

#simulate printing all designs until none are left
#move each design to completed_models after printing
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)
#display all completed models
print("\nThe following models have been completed: ")
for design in completed_models:
    print(design)