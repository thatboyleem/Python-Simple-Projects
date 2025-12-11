favorite_languages = {
    'jen':'python',
    'sarah': 'C',
    'edward':'rust',
    'phil':'python',
}

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll")

#looping through all the values in a dictionary
#u can use a values method to return a series of values

print("\nThe following languages have been mentioned: ")
for language in favorite_languages.values(): #this method might include repeats
    print(language.title()) 
print('\n')
#to see a each language chosen without repetition use
for language in set(favorite_languages.values()):
    print(language.title())