squares = [value**2 for value in range(1,11)]
print(squares)

for value in range(1,21):
    print(value)

numbers = list(range(1,1000001))
maxi= max(numbers)
mini= min(numbers)
Sum=sum(numbers)
print(maxi, mini)
print(Sum)

odd_numbers= list(range(1, 21, 2))
print(odd_numbers)

multiples_3 = [value*3 for value in range(3, 31)]
print(multiples_3)

cubes=[]
for value in range(1,11):
    cube= value**3
    cubes.append(cube)
print(cubes)

cubes =[value**3 for value in range(1,11)]
print(cubes)
   