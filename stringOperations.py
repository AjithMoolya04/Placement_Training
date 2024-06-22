input_string=input("enter a string")

#string length
print("length of the string",len(input_string))

#convert to uppercase
print("uppercase:",input_string.upper())
print(input_string.isupper())

#convert to lower case
print("lowercase:",input_string.lower())
print(input_string.islower())

#capitalize the string
print("capitalized:",input_string.capitalize())
print("capitalized every word:",input_string.title())

#count occurance of the substring
substring=input("enter the substring to count the occurance")
print("occurance of",substring,"in the string:",input_string.count(substring))

#check if the string starts with a specific substring
prefix=input("enter thr prefix to check if the string starts with it:")
print("strat with ",prefix,":",input_string.startswith(prefix))

#check if the string ends with a specific substring
suffix=input("enter a suffix to check if the string ends wih it:")
print("ends with",suffix,":",input_string.endswith(suffix))

#replace a substring with another substring
old_substring=input("enter the substring to replace:")
new_substring=input("enter the replacement substring:")
print("after replacement:",input_string.replace(old_substring,new_substring))

#split the string into a list of substring
delimiter=input("enter the delimiter to split the string:")
print("split string:",input_string.split(delimiter))

#join a list of substring into a single string
substrings=input("enter the substring to join (seperated by space):").split()
join_delimiter=input("enter the delimiter to join the substring:")
print("joined string:",join_delimiter.join(substring))

#the strip() method removes any whitespace from the begining or the end:
print(input_string.strip())
#PRINT(input_string.istrip())
#print(input_string.rstrip())
#print(input_string.rjust())
print(input_string.rfind("l"))
print(input_string.rindex("l"))
 