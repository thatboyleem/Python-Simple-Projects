#to modify a list as you walk through it u need a while loop
#moving items from one list to another

unconfirmed_users = ['alice', 'brian','candace']
confirmed_users = []

#verify users until there are no unconfirmed users
#move each verified user to the list of confirmed users

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying User: {current_user.title()}")
    confirmed_users.append(current_user)
#display all confirmed users
print("\n The following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())