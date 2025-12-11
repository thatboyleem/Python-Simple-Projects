from ntpath import join


pet1={
    'type': 'cat',
    'owner': 'solomon',
}
pet2 ={
    'type': 'Dog',
    'owner':'louis',
}
pet3 ={
    'type': 'snake',
    'owner':'Eve'
}

pets =[pet1, pet2, pet3]
for pet in pets:
    print(f"Type: {pet['type'].title()}\nOwner: {pet['owner'].title()}")
    print('\n')

fav_numbers ={
    'saleem' : [00, 23, 24],
    'farash':[47, 35, 15],
    'nabil': [3, 7],
    'mark':[10]
}
for name, numbers in fav_numbers.items():
    print(f"{name.title()}'s favorite numbers are: ")
    for number in numbers:
        print(join((str(number))))
    