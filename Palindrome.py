s =input("enter the string: ")
j=[]
r=[]
for i in range(len(s)):
    if s[i].isalnum():
        j.append(s[i].lower())
print(j)
r=j[::-1]
print(r)
if r==j:
    print(True)
else:
    print(False)
