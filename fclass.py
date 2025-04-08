class person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def names(self):
        print(f"my first name is {self.fname} and my last name is {self.lname}")
class customer(person):
    def __init__(self,fname,lname,balance=0):
   
        self.fname = fname
        self.lname = lname
        self.balance = balance
    def set_balance(self,balance):
        self.balance = balance
    def names(self):
        print(f"my first name is {self.fname} and my last name is {self.lname} balance is {self.balance}")
        
        
p1= person('ian','derick')
p2=person('benja','njau')
p3 = customer('john','doe',600)
p1.names()
p3.names()
        
