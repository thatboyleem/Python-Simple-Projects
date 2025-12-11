
answers = {}
polling_active = True

while polling_active:
    name = input("What is your Name?: ")
    response= input("\nwhat is your dream vacation spot?: ")

    answers[name]= response
    
    redo = input("\nWould you like to answer again?(yes/no): ")
    if redo == 'no':
        polling_active = False
print("-------RESULTS-------")
for name, response in answers.items():
    print(f"{name}'s dream vacation Spot is {response}!")
