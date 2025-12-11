#sorting a list permanently with sort()
cars = ['audi', 'bmw', 'subaru', 'toyota']
cars.sort()
print(cars)

#sort in reverse alphabetical order
cars.sort(reverse=True)
print(cars)

#sorting a list temporarily with sorted()
cars2=['nissan', 'prado', 'jeep', 'land cruiser', 'maserati']
print("here is the original list : ")
print(cars2)

print("here is the sorted list: ")
print(sorted(cars2, reverse=True))
print(sorted(cars2))

print("\n heres the original again: ")
print(cars2)

#printing a list in reverse order
print(cars)
cars.reverse()
print(cars)

#finding the length of list
length=len(cars2)
print(length)
