#similar to list but cant be modified like in the case of list i.e its immutable

dimensions = (200, 50) #tuples uses parenthesis instead
print(dimensions[0])
print(dimensions[1])

my_t=(3,) #defining a tuple with one element needs to be trailed by a comma.

#looping thru tuples
for dimension in dimensions:
    print(dimension)

#writing over a tuple
dimensions=(200, 50)
print('original dimensions: ')

for dimension in dimensions:
  print(dimension)
print('\n')

dimensions=(400, 20) #assigns new values to dimensions
print("new dimensions: ")
for dimension in dimensions:
   print(dimension)