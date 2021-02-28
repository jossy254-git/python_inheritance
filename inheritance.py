#creating a parent class.
class user:
    def __init__(self, name):
        self.name = name

    def login(self):
        print(self.name)

#creating a child class:
class register(user):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email
    
    def regi(self):
        print("user email is: " + self.email)

x = register("joseph waweru", "joe.wesh49@gmail.com")
x.login()
x.regi() 