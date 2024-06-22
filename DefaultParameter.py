# #default parameter passing
# def myfun(x,y):
#     print("x:",x)
#     print("y:",y)
# myfun(10,50)

# #keyword arguemnets
def student(firstname,lastname):
    print(firstname,lastname)

student(firstname='john',lastname='snow')
student(lastname='snow',firstname='john')

#agrument
def myFun(*argv):
    print(argv)

print(myFun("hello",'Welcome','to','India'))

#anonymous function
def cube(x):
    return x*x*x
cube=lambda x:x*x*x

print(cube(7))
print(cube(7))
