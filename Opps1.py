class person(object):
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber
        
    def display(self):
        print(self.name)
        print(self.idnumber)
        
    def details(self):
        print("my name is {}".format(self.name))
        print("ID number {}".format(self.idnumber))
        
#child class
class employee(person):
    def __init__(self,name,idnumber,salary,post):
        self.salary=salary
        self.post=post
        person.__init__(self,name,idnumber)
        
    def details(self):
        print("my name is {}".format(self.name))
        print("ID number is {}".format(self.idnumber))
        print("Post: {}".format(self.post))
        
a=employee('Rahul',8050,220,"intern")
a.display()
a.details()