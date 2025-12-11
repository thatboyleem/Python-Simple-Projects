class User:
    """This class is to store and create a user object."""
    def __init__(self, first_name, last_name, age, dob):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.dob = dob
        self.login_attempts = 0

    def describe_user(self):
        """This method prints all the user's information."""
        print(f"The user info is: \n\tName: {self.first_name} {self.last_name}")
        print(f"\n\tAge: {self.age} \n\tDate of birth: {self.dob}")

    def greet_user(self):
        """This method prints a greeting message to the user."""
        print(f"Welcome {self.last_name} {self.first_name}, glad to have you!")

    def increment_login_attempts(self):
        """This method increments login attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """This method resets login attempts to 0."""
        self.login_attempts = 0

# Creating a user instance
user1 = User("John", "Doe", 30, "1995-06-15")

# Displaying user information
user1.describe_user()
user1.greet_user()

# Testing login attempts
print(f"Login attempts: {user1.login_attempts}")
user1.increment_login_attempts()
user1.increment_login_attempts()
print(f"Login attempts after incrementing: {user1.login_attempts}")
user1.reset_login_attempts()
print(f"Login attempts after resetting: {user1.login_attempts}")
