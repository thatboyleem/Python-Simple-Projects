names_poll = ['saleem', 'fadila', 'imraan', 'mucktar', 'solange', 'jen', 'phil']
favorite_languages = {
    'jen':'python',
    'sarah': 'C',
    'edward':'rust',
    'phil':'python',
}
for name in names_poll:
    if name in favorite_languages.keys():
        print(f'Thank you {name.title()} for taking the poll.')
    else:
        print(f'{name.title()} please take the poll')