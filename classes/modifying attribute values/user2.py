class User:
    """this class is to store and create a user object"""
    def __init__(self, first_name, Last_name, age, dob):

        self.first_name = first_name
        self.Last_name = Last_name
        self.age = age
        self.dob = dob
        self.login_attempts = 0

    def describe_user(self):
        """this method is used to print all the users information"""
        print(f"The user info is: \n\tName: {self.first_name} {self.Last_name}")
        print(f"\n\tAge: {self.age} \n\tDate of birth: {self.dob}")
    def greet_user(self):
        """this method prints a greeting message to the user"""
        print(f"Welcome {self.Last_name} {self.first_name}, glad to have you!")
    
    def increment_login_attempts(self):
        """this function increments login attempts by 1"""
        self.login_attempts+=1
        return self.login_attempts

    def reset_login_attempts(self):
        """this function resets the login attempts to 0"""
        self.login_attempts=0

user1= User('saleem', 'Ahmed', 25, '4-08-2000')
user1.describe_user()
user1.increment_login_attempts()
print(f"login Attempts: \t{user1.login_attempts}")
user1.reset_login_attempts()
print(f"login Attempts: \t{user1.login_attempts}")
print(f"{user1.increment_login_attempts()}")