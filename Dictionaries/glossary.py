glossary = {
    'list' : 'used to store a number of objects of which can be changed dynamically',
    'Tuples':'similar to list but their values are fixed once defined and cant be modified',
    'Loops' : 'can be used for checking equality and for going over items in a list',
    'if-elif-else': 'Used to check for multiple cases or situatons',
    'dictionary':'store an infinite amount of key-value pair informaton',
}
'''print(f"List:\n {glossary['list']}")
print(f"Tuples:\n {glossary['Tuples']}")
print(f"Loops:\n {glossary['Loops']}")
print(f"If-elif-else:\n {glossary['if-elif-else']}")
print(f"dictionary:\n {glossary['dictionary']}")'''
glossary['dictionary looping']='You can loop through a dictionary using items() method or through the keys() method or values() method'
glossary['polling']= 'asking people for their opinions on certain things'
for key, value in glossary.items():
    print(f"{key.title()}\n\t{value}")

