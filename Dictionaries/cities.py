cities = {
    'Tokyo' : {
        'country':'Japan',
        'Population': 14200000,
        'Fun fact': 'home to the worlds busiest pedestrian crossing, the shibuya crossing'
    },
    'New York City':{
        'country': 'USA',
        'Population':8300000,
        'Fun fact': 'The city that never sleeps due to its vibrant nightlife and 24/7 activity',
    },
    'Paris':{
        'country': 'France',
        'Population': 2100000,
        'Fun fact': 'Called the city of light as it was one of  the first cities to have street lighting',
    }
}

for city, city_info in cities.items():
    print(f"{city}:")
    info = f"\t Country:{city_info['country']} \n\t Population:{city_info['Population']}"
    print(info.title())
    print(f"\tFun Fact:{city_info['Fun fact']}")