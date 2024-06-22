#read the name  and year of birth of a person  and calculate his age in 2024

year=int(input("enter the year of birth\n"))
name=input("enter the name\n")
cyear=2024
age=cyear-year
print("the person",name ,"born in",year," is ",age,"age")
for i in range(1,6):
    if (i==3):
        break
    print(i)
