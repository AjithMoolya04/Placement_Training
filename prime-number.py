# check if a number is prime or n not 
num=int(input("enter the number\n"))
for i in range( 2, num):
    if (num%i==0):
        print("not prime")
        break
    else:
        print("prime number")
