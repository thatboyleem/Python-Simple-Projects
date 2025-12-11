car = input("what kind of rental car would you like sir: ")
print(f"let me see if i can find you a {car}.")

people = input("how many of you guys are there please: ")
people = int(people)

if people >= 8:
    print("\n You guys are gonna have to wait for a table")
else:
    print("\n Your table is ready")