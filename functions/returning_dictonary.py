def build_person(first_name, last_name):
    """Returna dictionary of information about a person"""
    person = {'first': first_name, 'Last':last_name}
    return person
musician = build_person('jimi', 'hendrix')
print(musician)

