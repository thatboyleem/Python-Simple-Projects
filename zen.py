#import this
bicycles =['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-2].title()) #returns the second item from the end of the list, python uses -1 to return the last element in a list.

#using the first value in a list
message=f"my first bicycle was a {bicycles[0].title()}"
print(message)

names=['saleem', 'nabil', 'salman', 'nawas', 'faaris']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[-1])
message=f'Hello {names[0].title()}, i hope u doing well'
print(message)

cars =['bugati', 'ferari', 'lanborghini urus']
print(f"one day i'll own a {cars[1].title()}")

motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles)

motorcycles[0]= 'brabus' #add brabus to the 1st position

motorcycles.append('ducati') #add element to the end of the list
motorcycles.append('yamaha')
motorcycles.append('suzuki')

#inserting elements to a list
motorcycles.insert(0, 'senke') #insert method opens a space at position 0 and the stores the value 'senke' at the location

#removing elements from a list
del motorcycles[0]

#removing an item using the pop method
popped_motorcycle= motorcycles.pop()
#print(popped_motorcycle)
last_owned = motorcycles.pop()
print(f'the last motorcycle i owned was a {last_owned.title()}')

#removing by value
motorcycles.remove('honda')

#print(motorcycles)