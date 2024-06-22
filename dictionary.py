
my_dict11={"name":"Ford","model":"Mustang","year":1964}
my_dict22=dict(name="john",age=36,country="India")
print(my_dict11)


#creating the empty list
my_dict={}

#adding key and value to the dictionary
my_dict["name"]="alice"
my_dict["age"]=30
my_dict["city"]="new york"

print("Initial dictionaru:",my_dict)

#accessing the values
print("name:",my_dict["name"])
print("Age:",my_dict["age"])

x=my_dict.keys()
print(x)

y=my_dict.values()
print(y)

z=my_dict.items()
print(z)

m=my_dict.get("city")
print(m)

#
for x in my_dict:
    print(x)
    
for x in my_dict:
    print(my_dict[x])
    
#iterating over keys
print("keys:")
for key in my_dict.keys():
    print(key)
    
#iterating over the value
print("values:")
for value in my_dict.values():
    print(value)
    
#iterating over key-value pairs
print("key-value Pairs:")
for key,value in my_dict.items():
    print(key,":",value)

#checking if a key exists 
if "name" in my_dict:
    print("'name' exists in the dictionary")
else:
    print("'name' does not exist in the dictionary")
    
#modifing the value of 
my_dict['age']=35
print("modified age:",my_dict['age'])

my_dict.update({"age":45})

#adding the dictionary
my_dict["color1"]="fair"
print(my_dict)

my_dict.update({"color2":"dark"})

#removing a key-vlaue pair
removed_value=my_dict.pop('city')
print(removed_value)
print(my_dict)

my_dict.popitem()
print(my_dict)
my_dict.clear()
print("Dictionary after clearing ",my_dict)

del my_dict


