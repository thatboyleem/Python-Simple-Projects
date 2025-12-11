person1 ={
    'name' : 'saleem Ahmed',
    'id': 57,
    'section': 2
}
person2={
    'name': 'Farash Idriss',
    'id': 61,
    'section': 1
}
person3 ={
    'name': 'Abasse abdella',
    'id': 61,
    'section':2,
}
persons = [person1, person2, person3]

for person in persons:
    print(f"Student name: {person['name']}\nStudent id: {person['id']}\nStudent Section: {person['section']}")
