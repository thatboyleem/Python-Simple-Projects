#looping through all key-value pairs 
user_0 = {
    'username': 'efermi',
    'first': 'enricho',
    'last':'femi',
}
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}") #to loop through a dictionary u create names for the two variables that will hold the key and value in each key-value pair

#looping through all the keys in a dictionary
favorite_languages = {
    'jen':'python',
    'sarah': 'C',
    'edward':'rust',
    'phil':'python',
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
for name in favorite_languages.keys():
    print(name.title()) #looping through keys in a dictionary  (for name in favorite_languges: this syntax will still work)

#access a value associated with any key
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f'hi {name.title()}.')
    if name in friends:
        language= favorite_languages[name].title()
        print(f"\t{name.title()}, i see you like {language}!")
if 'erin' not in favorite_languages.keys():
    print("Erin please take our poll")
