# read the marks of a student if marks>80 distinction , if between 60 -80 (pass),if it is <60 fail

marks=int(input("enter the marks\n"))
if marks>80:
    print("distinction")
elif(marks>=60 and marks<=80):
    print("pass")
elif(marks<60):
    print("fail")
else:
    print("invalid")