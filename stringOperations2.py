# string formating
age=36
name=input("enter the name\n")
print("my name is {} and i am {} year old".format(name,age))

#reversing the string
str="Hello World"
print("original string",str)
print("reversed string",str[::-1])

#or
def reverse_string(str):
    rev=" "
    i=len(str)
    while(i>0):
        rev=rev+str[i-1]
        i=i-1
    return rev


str1="Hello World"
print("the reversed string is:",reverse_string(str1))


    