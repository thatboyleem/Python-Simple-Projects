#using for loops
magicians =['alice', 'david', 'carolina']
for magician in magicians: #used to automate repetitive tasks
    print(magician)

#doing more work within a list
for magician in magicians:
    print(f'{magician.title()}, that was a great trick!')
    print(f'I cant wait to see your next trick, {magician.title()}.\n')
print("thank you everyone, that was a great show!")

