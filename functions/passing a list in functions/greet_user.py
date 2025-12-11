#the following example sends a lists of names to a function called greet users
def greet_users(names):
    """print a greeting for every user in the list"""
    for name in names:
        msg = f"hello, {name.title()}!"
        print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)