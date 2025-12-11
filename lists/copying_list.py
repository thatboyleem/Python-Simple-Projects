#u can copy an entire list by making a slice in which you've omitted a start and a finish index
my_games=['basketball', 'tennis', 'football', 'skating', 'roller_blading']

new_games= my_games[:]
print('my best games are: ')
print(my_games)
print('\n')

print('the new games are: ')
print(new_games)

my_games.append('dancing')
new_games.append('ballet')

print(my_games)
print(new_games)

skills=['marking', 'reading', 'writing', 'critical thinking', 'effective communication']
print('the first three items in the list are: ')
for skill in skills[0:3]:
    print(skill.title())
print('\n')
print("the middle three items are: ")
print(skills[1:4])
print("\n the last three items are: ")
print(skills[-3:])

add_skills= skills[:]

skills.append("adaptive learning")
add_skills.append("fast learner")

print(skills)
print(add_skills)

print('\n')
for skill in skills[0:]:
    print(skill)

print('\n')
for skill in add_skills[0:]:
    print(skill)