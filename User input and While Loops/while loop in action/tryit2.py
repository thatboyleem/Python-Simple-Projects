current_users = ['john', 'mary', 'steve', 'david', 'alice']
new_users = ['John', 'amy', 'Steve', 'michael', 'sarah']

current_users_lower = [user.lower() for user in current_users]

index = 0
active = True

while active and index < len(new_users):
    new_user = new_users[index]
    if new_user.lower() in current_users_lower:
        print(f"The username '{new_user}' is already taken. Please choose a new username.")
    else:
        print(f"The username '{new_user}' is available.")
    index += 1
    if index >= len(new_users):
        active = False
