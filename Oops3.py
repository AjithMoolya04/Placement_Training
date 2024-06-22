class super:
    #public data member
    var1=None
    
    #protected data member
    _var2=None
    
    #private data member
    __var3=None
    
    #constructor
    def __init__(self,var1,var2,var3):
        self.var1=var1
        self._var2=var2
        self.__var3=var3
        
    #public member function
    def displaypublicmembers(self):
        print("Public Data Member:",self.var1)     #printing the public member
        
    #protected member function
    def _displayprotectedmember(self):
        print("protected Data Member: ",self._var2)      #printng the protected member
        
    #private member function
    def __displayprivatemember(self):
        print("private data member :",self.__var3)      #printing the private member
        
        
    #public member function
    def accessprivatemember(self):
        self.__displayprivatemember()           #accessing the private member through public member function
        
class sub(super):
    #constructor
    def __init__(self,var1,var2,var3):
        super.__init__(self,var1,var2,var3)
        
    #public member function
    def accessprotectedmember(self):
        self._displayprotectedmember()    #accessing the protected member function of super class
        
obj=sub("hello","all","people !")
    
    #calling public member functions of the class
obj.displaypublicmembers()
obj.accessprotectedmember()
obj.accessprivatemember()

#object can access protected member
print("object is accessing protecetd member:",obj._var2)

#object can not access priate member,so it will generate attribute

        
    
    
        