#u can prompt a user for as much input as you want
responses = {}
polling_active = True

while polling_active:
    name = input("\n What is your name?: ")
    response= input("Which mountain would you like to climb someday?: ")

    #store response in dictionary
    responses[name]= response

    #find out if annyone else is going to take the poll
    repeat = input("Would you like to let another person respond?(yes/no): ")
    if repeat == 'no':
        polling_active = False
#polling is complete. Show the results
print('\n.....Poll Results......')
for name, response in responses.items():
    print(f"{name} would like to climb {response}")