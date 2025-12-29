from car import car, electricCar

my_leaf = electricCar('nissan', 'leaf', 2024)
my_mustang = car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())
print(my_leaf.get_descriptive_name())