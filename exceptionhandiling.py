# #
# def convert_to_integer(string):
#     try:
#         number=int(string)
#         print("Integer Value:",number)
#     except ValueError:
#         print("error: invalid integer format!")
        
# def main():
#     string=input("enter ")
#     convert_to_integer(string)
    
# if __name__=="__main__":
#     main()

# #get positive number
# def get_positive_integer():
#     while True:
#         try:
#             num=int(input("enter a positive integer:"))
#             if num<=0:
#                 raise ValueError("Not a positive integer")
#             return num
#         except ValueError as e:
#             print("Error:",e)
# postive_integer=get_positive_integer()
# print("You Entered:",postive_integer)

# class mycustomerror(Exception):
#     def  __init__(self,message):
#         self.message=message
    
# try:
#     raise mycustomerror("This is a custom error message")
# except mycustomerror as e:
#     print("custom err caught:",e.message)

# def access_list_element(lst,index):
#     try:
#         value=lst[index]
#         print("vlaue at index",index,'is',value)

#     except IndexError:
#         print("Error:Index out of Range")
# my_list=[1,2,3,4,5]
# index=int(input("enter the index to acces "))
# access_list_element(my_list,index)

# def access_dictionary_value(dictionary,key):
#     try:
#         value=dictionary[key]
#         print("Vlaue for key",key,'is:',value)
#     except KeyError:
#         print("Error:key not found!")

# my_dict={'a':1,'b':2,'c':3}
# key=input("enter a key to acces")
# access_dictionary_value(my_dict,key)
