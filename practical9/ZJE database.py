class Staff(object):
    def __init__(self,firstname,lastname,location,role):
        self.firstname=firstname
        self.lastname=lastname
        self.location=location
        self.role=role
        self.fullname=self.firstname + ' ' + self.lastname
a=Staff('Yiran','Zhou','China','student')
#Take an example
print(a.fullname,a.location,a.role)
