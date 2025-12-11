#store information about the a pizza being ordered
pizza = {
    'crust':'thick',
    'toppings':['mushrooms', 'extra cheeese'],
}
#summarize order
print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings: ")
for topping in pizza['toppings']: #use a list when u want more than one value to be associated with a key.
    print(f"\t{topping}")

favorite_languages = {
    'jen' : ['python', 'rust',],
    'sarah': ['C'],
    'edward': ['rust', 'go'],
    'phil':['python', 'hashkell'],
}
for name, languagues in favorite_languages.items():
    print(f"\n {name.title()}'s favorite Languages are: ")
    for language in languagues:
        print(f"\t{language.title()}")