#write a program to  genaerate  prime number 1 to n
s=int(input("enter the starting number"))
e=int(input("enter the ending numebr"))
count=0

for num in range(s,e+1):
    for i in range(2,num):
        if(i==1 &i==0):
            print('not prime')
        else:
            if(num%i==0):
                break
    else:
        print(num)  
        count+=1
             
print("total  number of prime number=",count)