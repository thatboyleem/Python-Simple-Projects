from pyclbr import Class


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
class Admin(User):
    """this class represents an admin user, inheriting from User"""
    def __init__(self, first_name, Last_name, age, dob):
        super().__init__(first_name, Last_name, age, dob)
        self.privileges = Privileges()


class Privileges:
    """this class represents privileges for an admin user"""
    def __init__(self, privileges=None):
        if privileges is None:
            privileges = []
        self.privileges = privileges

    def show_privileges(self):
        """this method displays the admin's privileges"""
        print(f"Admin Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

user1= User('saleem', 'Ahmed', 25, '4-08-2000')
user2= User("manka'a", "cindy", 23, '05-9-2003')
user1.describe_user()
user2.describe_user()
user1.greet_user()
user2.greet_user()

saleem_admin = Admin('saleem', 'Ahmed', 25, '4-08-2000')
saleem_admin.describe_user()
saleem_admin.privileges.privileges = ['can add post', 'can delete post', 'can ban user']
saleem_admin.privileges.show_privileges()

