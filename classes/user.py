class User:
    """this class is to store and create a user object"""
    def __init__(self, first_name, Last_name, age, dob):

        self.first_name = first_name
        self.Last_name = Last_name
        self.age = age
        self.dob = dob

    def describe_user(self):
        """this method is used to print all the users information"""
        print(f"The user info is: \n\tName: {self.first_name} {self.Last_name}")
        print(f"\n\tAge: {self.age} \n\tDate of birth: {self.dob}")
    def greet_user(self):
        """this method prints a greeting message to the user"""
        print(f"Welcome {self.Last_name} {self.first_name}, glad to have you!")

user1= User('saleem', 'Ahmed', 25, '4-08-2000')
user2= User("manka'a", "cindy", 23, '05-9-2003')
user1.describe_user()
user2.describe_user()
user1.greet_user()
user2.greet_user()
