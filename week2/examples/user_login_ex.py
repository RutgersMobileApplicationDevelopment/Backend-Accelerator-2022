"""
Before we write a login function…
Create class to store username and password hash
Store passwords as hashes! (import bcrypt)

Now, let’s write a login function for our class…
Takes a user inputted password
Hashes the inputted password
Check the password against a stored hash
Login if username and password match
"""

class UserLogin:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.logged_in = False

    def login(self, password):
        self.logged_in = (password == self.password)
        return (password == self.password)

UserLogin("ben",b's$cret12')