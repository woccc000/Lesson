
class UserName:
    
    def __init__(self):
        self.name = 'Max'
        self.age = 19
        self.imail = 'good@jsdf.com'
    
    def __str__(self):
        return "User: {}, Age: {}, Imail: {}".format(self.name, self.age, self.imail)

    
men = UserName()
men.name = "Masha"
men.age = 17
men.imail = "sgdfgdfg@sdfsd.com"
print(men)


