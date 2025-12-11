favorite_languages = {
    'jen':'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',

}

language = favorite_languages['sarah'].title() #use this syntax to pull sarahs favorite language from the dictionary
print(f"sarah's favorite language is {language}.")

#using get() to access values
alien_0 = {'color':'green', 'speed': 'slow'}
#the get() method requires a key as a first argument
point_value = alien_0.get('points', 'no point value is assigned') #python will print None if default value is not given in the arguments
print(point_value)
