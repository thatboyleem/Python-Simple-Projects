def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster') #equivalent function calls
describe_pet(pet_name='scott') #equivalent function call
describe_pet('blitz', 'turtle')

describe_pet(pet_name='bolt', animal_type='cat') #overwrite the default value 