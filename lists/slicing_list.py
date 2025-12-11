#slicing a list
players = ['charles', 'messi', 'maradona', 'neymar', 'ronaldo']
print(players[0:3]) #like in range u specify the start and end of the part of the list u want to work with it also has the of-by-one behaviour

print(players[1:4])
print(players[2:5])

print(players[:4]) #without starting index, python starts at the begining of the list
print(players[2:]) #include the last item in the list

print(players[-3:]) #output the last 3 players in the list

#looping through a slice
print('here are the first three players on my team')
for player in players[:3]:
    print(player.title())

