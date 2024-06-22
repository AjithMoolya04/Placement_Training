#program to find upper case and lower case letters in a sentence
input=input(" Enter hte string=")
upper_case=0
lower_case=0
for i in input:
  if i.isupper():
    upper_case+=1
  elif i.islower():
    lower_case+=1
print("upper case:",upper_case)
print("lower case:",lower_case)
