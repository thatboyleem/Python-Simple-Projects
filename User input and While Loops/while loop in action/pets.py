#removing all instances of specific values from the list
pets = ['dog', 'cat', 'dog', 'gold fish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)