#using the range() function
for value in range(1, 5): #also has the off-by-one behaviour of indexing
    print(value) #nb: u can also pass one argument in range()
print("\n")
for value in range(1, 6):
    print(value)
print('\n')
for value in range(6):
    print(value)

#using range to make a list of numbers
print('\n')
numbers = list(range(1,6))
print(numbers)

#using range to tell python to skip numbers in a given range
even_numbers= list(range(2, 11, 2))
print(even_numbers)

#make a square of numbers
#(**) in python represents exponent
squares =[]
for value in range(1,11):
    square=value**2
    squares.append(square) #or u can remove square = value**2 and just do squares.append(value**2)
print(squares)

#simple statistics
digits=[1,2,3,4,5,6,7,8,9,0]
mini=min(digits)
maxi=max(digits)

print(f'{maxi}')
print(f'{mini}')
print(sum(digits))