def build_person(first_name, last_name, age=None): #none is a placeholder value, it evaluates to false in conditional statements
    """Returna dictionary of information about a person"""
    person = {'first': first_name, 'Last':last_name}
    if age:
        person['age']= age
    return person
musician = build_person('jimi', 'hendrix', age=27) 
print(musician)
