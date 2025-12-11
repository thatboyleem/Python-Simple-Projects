users = {
    'aeinstein':{
        'first': 'albert',
        'last': 'einstein',
        'Location': 'princeton',
    },
    'mcurie':{
        'first' : 'marie',
        'last' : 'curie',
        'Location' : 'paris'
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['Location']

    print(f"\t Full name : {full_name}")
    print(f"\tLocation: {location.title()}")