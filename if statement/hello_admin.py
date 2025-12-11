usernames =['saleem','farash','mike','noel','yuyun','admin']

if usernames: #checking to see if list is not empty.
  for name in usernames:
    if name=='admin':
        print(f'Hello {name.title()}, would you like to see the status report')
    else:
        print(f"Hello {name.title()}, thank you for loggin in again")
else:
   print("we need to find users") #prints this if list is empty

current_users = ['emma', 'trina', 'danny', 'sergio', 'ramos']
new_users = ['mark', 'brandon', 'emma', 'gina', 'boris']

'''for name in current_users:
   if name.upper() and name.lower() in new_users:
      print(f"sorry, Enter a new User_name, {name.title()} has already been taken")
   else:
     print(f"{name.title()}, the Username is available")'''
new_users= [name.lower() for name in new_users]
for name in new_users:
   if name in current_users:
      print(f"sorry, {name.title()} is already taken")
   else:
      print(f"Welcome, {name.title()}, is available")
