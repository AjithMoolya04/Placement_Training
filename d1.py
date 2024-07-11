# name=input("enter your name\n")
# print(name)
# print("my name is "+name)

#read the name  and year of birth of a person  and calculate his age in 2024

# year=int(input("enter the year of birth\n"))
# name=input("enter the name\n")
# cyear=2024
# age=cyear-year
# print("the person",name ,"born in",year," is ",age,"age")
# for i in range(1,6):
#     if (i==3):
#         break
#     print(i)

# read the marks of a student if marks>80 distinction , if between 60 -80 (pass),if it is <60 fail

# marks=int(input("enter the marks\n"))
# if marks>80:
#     print("distinction")
# elif(marks>=60 and marks<=80):
#     print("pass")
# elif(marks<60):
#     print("fail")
# else:
#     print("invalid")

# check if a number is prime or n not 
#write a program to  genaerate  prime number 1 to n
#write program, if the number is strong number or not-the  sum of factorial of individual digit is equal to the number it self
#write program  if n is armstrong or not 
#write a program to spy of the number
#check if n number is happy  number or  not
#write a program to check if number is neon number or not
#write a program to genaerate the fabinacci series and fabonacci number of a given number 
#write a program check if the numnber is palindrome or  not
 #write a program to find factorial of a number
#write a program to check leap yaer or not


# check if a number is prime or n not 
# num=int(input("enter the number\n"))
# for i in range( 2, num):
#     if (num%i==0):
#         print("not prime")
#         break
#     else:
#         print("prime number")



#write program, if the number is strong number
# num=int(input("enter the number\n"))
# sum=0
# temp=num
# while(num):
#     i=1
#     f=1
#     r=num%10
#     while(i<=r):
#         f=f*i
#         i=i*1
#     sum=sum+f
#     num=num//10
# if temp==sum:
#     print("the number is strong")
# else:
#     print("the number is not strong number")



#write program  if n is armstrong or not 
# num=int(input("enter the number\n"))
# order=len(str(num))
# sum=0
# temp=num

# while temp>0:
#     digit=temp%10
#     sum+=digit**order
#     temp//=10
# if num==sum:
#     print(num,"is an armstrong number")
# else:
#     print(num,"ia not an armstrong number")



#write a program to check if number is neon number or not
# num=int(input("enter the number\n"))
# sq=num*num
# temp=num
# sum=0

# while(sq!=0):
#     r=sq%10
#     sum=sum+r
#     sq=sq//10
# if(sum==temp):
#     print("neon")
# else:
#     print("not neon")


#write a program to spy of the number
# num=int(input('enter the number \n'))
# temp=num
# sum=0
# p=1
# while(num>0):
#     t=num%10
#     sum=sum+t
#     p=p*t
#     num=num//10
# if (sum==p):
#     print(temp,"is a spy  number!")
# else:
#     print(temp,"is spy  number")



# write a program to check if  number is happy  number or  not

# def ishappy(num):
#     r=0
#     while(num!=0):
#         d=num%10
#         r+=d**2
#         num=num//10
#     return r
# num=int(input("enter the number "))
# res=num

# while(res!=1 and res!=4):
#     res=ishappy(res)

# if(res==1):
#     print("happay number ")
# else:
#     print("not a happy number")


# s=int(input("enter the starting number"))
# e=int(input("enter the ending numebr"))
# count=0

# for num in range(s,e+1):
#     for i in range(2,num):
#         if(i==1 &i==0):
#             print('not prime')
#         else:
#             if(num%i==0):
#                 break
#     else:
#         print(num)  
#         count+=1
             
# print("total  number of prime number=",count)


# n=int(input("enter  the number"))
# fib=0
# fib2=1
# print("fibonacci series of a given number",n,"is")


#write a python program to find best of two test avaerage marks out of 3 test marks accepted from the user
#develop a python  program to covert a binary  number into decimal ,octal and hexa decimal number using funtion

#defina a function F as Fn=Fn-1+Fn-2 write a python program whitch accepts a value for N (where N>0) as input and pass
#this val;ue to the fuction disply suitabler error meassge itf the condotion for input valuer is not followed

# write a python to check string similarity 



#write a python programm that accepts a sentence and finds the number of words,digits,upper case letter,lowercase letter 

# write a python   to make 
# *
# **
# ***
# ****
# *****
# ******

#write a programa to make pattern
#       *
#      **
#     ***
#    ****
#   *****

#write program to make a pattern
# ********
#   ******
#    *****
#     ****
#      ***
#       **
#        *

#write a python  programm to make a pattern
# *******
# *****
# ****
# ***
# **
# *

#write a python program  to make a pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
#writea program to make a pattern
# 1
# 2 2
# 3 3 3 
# 4 4 4 4
# 5 5 5 5 5
#write a program  to find a patterm
# * * * * * *
# *         *
# *         *
# *         *
# *         *
# * * * * * *
#write  a program 
# * * * * * *
# * *    *  *
# *    *    *
# *  *   *  *       
# * * * * * *
#write a  program
# 1 2 3 4
# 5 6 7 8 
# 9 10 11 12
# 13 14 15 16
#writa program
# A A A A A 
# A A A A A
# A A A A A 
# A A A A A


# patten-1
# n=int(input())
# for i in range(0,n):
#     for j in range(0,n):
#         print("*",end=" ")
#     print()

# patten-2
# n=int(input())
# for i in range(0,n):
#     for j in range(0,n):
#         if(j<=i)
#         print("*",end=" ")
#     print()


# pattern -3
# n=int(input())
# for i in range(0,n):
#     for j in range(0,n):
#         if i+j>=n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# patten-4
# n=int(input())
# for i in range(0,n):
#     for j in range(0,n):
#         if(j>=i):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# pattern-5
# n=int(input())
# for i in range(0,n):
#     for j in range(0,n):
#         if(i+j<=n-1):
#             print("*",end=" ")    
#     print()

# pattern-6
# n=int(input())
# for i in range(1,n):
#     for j in range(1,n):
#         if(j<=i):
#             print(i,end=" ")    
#     print()

# pattern-7
# n=int(input())
# for i in range(n):
#     for j in range(n):
#         if(i==0 or i==n-1 or  i+1==n-1 or j==0 or j==n-1 or j==i or i+j==n-1):
#             print("*",end=" ")   
#         else:
#             print(" ",end=" ") 
#     print()

# pattern-8
# n=int(input())
# k=1
# for i in range(n):
#     for j in range(n):
#             print(k,end=" ")   
#             k=k+1
#     print()

#factorial of  number
# num=int(input())
# fact=1
# if num<0:
#     print("sorry factorial does n ot exit for negative number")
# elif num==0:
#     print("factorial of is 0 of 1")
# else:
#     for i in  range(1,num+1):
#         fact=fact*i
#     print("factorial of a number ",fact)

#wap to read string from user and implement  the logic to remove the charectors whitch are at the odd number of the index

# s=input()
# res=""
# for i in range(0,len(s)):
#     if (i%2==0):
#         res+=s[i]
# print(res)
        
#wta program to swap to numbers using 3 variables

# a=input("enter the value of a\n")
# b=input("enter the value of b\n")
# temp=0
# temp=a
# a=b
# b=temp
# print("value of a=",a)
# print("value of b=",b)

# wta to find best of 2 avg marks out of 3 testmarks accepted from the user

# list=["apple","banana","cherry"]
# list[1:3]=["blackcuurent","watermelon"]
# print(list)

# lis=['apple','banana','cherry',"kiwi",'mango']
# newlist=[]
# for x in lis:
#     if "a" in x:
#         newlist.append(x)
# print(newlist)


# lis=['apple','banana','cherry',"kiwi",'mango']

# sort based on how the number close to 50(customised sort)
# def fun(n):
#     return abs(n-50)


# lis=[100,50,39,55,59]
# lis.sort(key=fun)
# print(lis)

# lis=[100,-50,-39,55,-59]
# for i in lis:
#     print(abs(i))

# lis=['Apple','Banana','Cherry',"kiwi",'mango']
# lis.sort(key=str.lower)
# print(lis)

# lis=[10,20,30,40,50]
# sum=0
# for i in lis:
#     sum+=i
# print(sum)
# avg=sum/len(lis)
# print(avg)


#count the nuknerv of accuremce of a given item in the list
#write a program, to count unique values in the list
#find out the duplicate removal list product using list comphrension
#write a programm to exreact element with the freeqenccy greater than k 
#write a program to test a list contained int range
#write a program to demonstrate list inj section and union
#write programm to merge to sorted list in to single sorted list
#find the largest sub array sum in the given list
#wta to partittion a list arround a given value such that all elelments less than the gievn values come before it and the all element greater then  tha given value come after it
#find the peak element in the list of integer.peak elemnt is an element that is grater than or equal to it neighbor
#wta 



#count the nuknerv of accuremce of a given item in the list
# def acc(lis,n):
#     count=0
#     for i in lis:
#         if (i==n):
#             count+=1
#     return count
# lis=[10,20,40,40,10,90,70,40]
# n=40
# print(acc(lis,n))


#write a program, to count unique values in the list

# lis=[10,20,40,40,10,90,70,40]
# count=0
# new=[]
# for i  in lis:
#     if i not in new:
#         new.append(i)
#         count+=1
# print(new,count)


#find out the duplicate removal list product using list comphrension
# lis=[1,2,3,4,5]
# product=1
# new=[]
# [new.append(x) for x in lis if x not in new]
# for i in new :
#     product*=i
# print("prodcut of the duplication removeal list: "+str(product))


#write a programm to exreact element with the freeqenccy greater than k 
# li=[8,9,8,9,8,8,5,5,4,5]
# k=2
# new=[]
# for i in li:
#     freq=li.count(i) 
#     if (freq>2 and i not in new ):
#         new.append(i)
# print(new)

#wta to test a list contains elements in the range
# lis=[4,6,5,4]
# i,j=3,10
# for  ele in lis:
#     if ele<i or ele>j:
#         print(False)
#     else:
#         print(True)

#write a program to demonstrate list inj section and union
# def list_union(lst1,lst2):
#     return list(set(lst1) | set(lst2))
# list1=[1,2,3,4,5]
# list2=[3,4,5,6,7]

#write programm to merge to sorted list in to single sorted list
# l1=[1,3,5,7,9]
# l2=[2,4,6,8,10]
# wh

#wta to partittion a list arround a given value such that all elelments less than the gievn values come before it and the all element greater then  tha given value come after it
# def part(lst,pivot):
#     less=[]
#     equal=[]
#     greater=[]
#     for i in lst:
#         if i<pivot:
#             less.append(i)
#         elif(i==pivot):
#             equal.append(i)
#         else:
#             greater.append(i)
#     return less+equal+greater
# lst=[3,4,1,5,9,2,6,5]
# pivot=4
# print("partioned list: ",part(lst,pivot))

#find the largest sub array sum in the given list
# lst=[-2,1,-3,4,-1,2,1,-5,4]
# sum=0
# cur=maxi=lst[0]
# for i in lst:
#     cur=max(i,cur+i)
#     maxi=max(maxi,cur)
# print(maxi)

#find the peak element in the list of integer.peak elemnt is an element that is grater than or equal to it neighbor
# def peak(num):
#     if not num:
#         return None
    
#     left,right=0,len(num)-1
#     while left<right:
#         mid=left+(right-left)//2
#         if num[mid]<num[mid+1]:
#             left=mid+1
            
#         else:
#             right=mid
            
#     return left
    
# listt=[1,2,1,3,5,6,4]
# print('peak element index',peak(listt))

# def create_tuple():
#     #creating tuple
#     tuple1=(1,2,3,4,5)
#     tuple2=("a","b","c","d","e")
#     tuple3=("apple","banana","cherry")
#     return tuple1,tuple2,tuple3

# def access_tupe_items(tuple1,tuple2):
#     #accesing the tuple items using positive and negative 
#     print("Tuple 1:",tuple1)
#     print("First element of the tuple 1:",tuple1[0])
#     print("last element of the tuple 1:",tuple1[-1])
#     print("tuple 2:",tuple2)
#     print("second first element of the tuple 2:",tuple2[1])
#     print("second last element of the tuple 2:",tuple2[-2])
#     print(tuple[0:5])

# def unpacking_tuple1(tuple3):
#     #unpacking the tuple
#     (green,yellow,red)=tuple3
#     print((green))
#     print(yellow)
#     print(red)
    
# def unpacking_tuple2(fruits):
#     #unpacking the tuple using asterisk
#     fruits=("apple","banana","cherry","straberry","raspberry")
#     (green,yellow,*red)=fruits
#     print(green)
#     print(yellow)
#     print(red)
    
# def change_tuple(tuple1,tuple2):
#     list1=list(tuple1)
#     list2=list(tuple2)
#     list1.append(6)
#     list2.append("c")
#     tuple1=tuple(list1)
#     tuple2=tuple(list2)
#     return tuple1,tuple2

# def loop_through_tuple(tuple1):
#     print("looping through tuple 1 usinh for loop")
#     for i in tuple1:
#         print(i)
        
#     print("looping through while loop and index number")
#     index=0
#     while(index<len(tuple1)):
#         print(tuple1[index])
#         index+=1
        
# def join_tuple(tuple1,tuple2):
#     #joining tuples 
#     tuple3=tuple1+tuple2
#     return tuple3     

# tuple1,tuple2,tuple3=create_tuple()
# access_tupe_items(tuple1,tuple2)
# print()

# unpacking_tuple1(tuple3)
# print()

# fruits=("apple","banana","cherry","strawberry","raspberry")
# unpacking_tuple2(fruits)
# print()

# tuple1,tuple2=change_tuple(tuple1,tuple2)
# print("After making changes:")
# access_tupe_items(tuple1,tuple2)
# print()

# tuple3=join_tuple(tuple1,tuple2)
# print("Joined tuple:",tuple3)

# mytup=(1,2,3)
# anothertup=tuple([4,5,6])
# print(mytup[0])
# print(mytup[-1])
# print(mytup[1:3])
# combinedtup=mytup+anothertup
# print(combinedtup)
# repeated_tuple=mytup*3
# print(repeated_tuple)
# print(2 in mytup)
# print(4 not in mytup)
# print(len(mytup))
# for item in mytup:
#     print(item)

# stringtotup=tuple('hello')
# print(stringtotup)
# listtotup=tuple([1,2,3])
# print(listtotup)
# print(mytup.count(2))
# print(mytup.index(3))
    
# tupofinteger=(5,2,8,1,3)
# sortedtup=tuple(sorted(tupofinteger))
# print('sorted tuple',sortedtup)

# tupleoftuple=((1,'apple'),(3,'orsnge'),(2,'banana'))
# sortedtuple=sorted(tupleoftuple,key=lambda x:x[1])
# print('sorted tuples',sortedtuple)

# list1=[1,2,3]
# list2=['a','b','c']
# ziptup=tuple(zip(list1,list2))
# print('zipped tuple',ziptup)

# from collections import namedtuple
# import math

# point=namedtuple('Point',['x','y'])

# point1=point(1,2)
# point2=point(4,6)

# distance=math.sqrt((point2.x-point1.x)**2+(point2.y-point1.y)**2)

# print("distance between point 1 and point 2:",distance)
# originaltup=(1,2,3,4,5)
# filetrtup=tuple(filter(lambda x :x%2==0,originaltup))
# print('filterred tuple',filetrtup)



# from functools import reduce

# def add(x,y):
#     return x+y

# original=(1,2,3,4,5)

# result=reduce(add,original)
# print("result of reducing the  tuple",result)



#add 
# set={"apple","banana","cherry"}
# set.add("orange")
# print(set)
# print("after add :",set)

# #update
# set={"apple","banana","cherry"}
# tropical={"pineapple","mango","papaya"}
# set.update(tropical)
# print("after update:",set)

# #remove
# set={"apple","banana","cherry"}
# set.remove("banana")
# print("aftre remove",set)



# def powerset(s):
#     result=[[]]
#     for ele in s:
#         result.extend([subset+[ele] for subset in result])
#     return [set(subset)for subset in result]
# input_set={1,2,3}
# powerset=powerset(input_set)
# print("power set : ",powerset)

# lst=[1,2,3,3]
# res=[]
# re=False
# for i in lst:
#     if i not in res:
#         res.append(i)
#     else:
#         re=True
#         break

#write a programm to convert decimal number to binary
#given an array of n numbers and another numbner the task is to check whesther or not to check whoose exact sum is x
# def summ(arry,target):
#     for i in range(0,len(arry)):
#         for j in  range(1,len(arry)):
#             if arry[i]+arry[j]==target:
#                 return i,j
            
# arry=[1,2,4,5,6,7,8]
# target=9
# print(summ(arry,target))



# dict={"alpa":[10,20,30]}
# print(dict.values)


#given an array of integer an number k find the counnt of dictance elemeent in every window of size in an array
# a=[1,2,1,3,4,2,3]
# k=4
# count=[]
# s=[]
# for i in range(0,len(a)):
#     for j in range(0,k):
#         s.append(j)
#         s=list(set(a))
# print(s)
# count.append(len(s))
# print(count)

# #an egulibrium index ia an index  the sumof elemnt in the lowewr indices is eqaul to hiher indices [-7,]

#you are given an m*n integer grid accounts where account of ij is the amount of money of ith customer has jth bank.the customers wealth is the amount of they have in all there bank accounts.the richest cusomer isthe customer that has the maximum well.

#given and array of size(n-1) such that it only contains dictinct integeer in the arnge off 1-n find the misising element inpur n=10 arr=[6,1,2,8,3,4,7,10,5]



# 1.Converting int to decimal 
# 2.Connecting a string into decimal
# 3.Reversing a string using extended slicing techniques 
# 4.Counting the vowels and consonants in a string
# 5.Counting the number of occurrences of a character into a string
# 6.Fibonacci series
# 7.Max and min in a list without using functions 
# 8.Comparing two strings for anagram 
# 9.Checking for palindrome using extended slicing
# 10.Printing a pyramid pattern using python

# 12.Given an array of strings words and width max width format the text such that each line has exactly max width characters and is fully justified you should pack your words in a greedy approach i.e., pack as many words that you can in each line. Pad extra spaces when necessary so that each line has exactly max width characters. Extra spaces between the words should be distributed as evenly as possible. If the number of space on a line does not divide evenly between the words, empty slots on the left will be assigned more space will be assigned on the right. For the last line of text it should be left JUSTIFIED and no space is inserted between the words 

# from textblob import TextBlob

# def analyze_sentiment(text):
#     analysis = TextBlob(text)

#     # Get polarity and subjectivity
#     polarity = analysis.sentiment.polarity
#     subjectivity = analysis.sentiment.subjectivity

#     # Determine sentiment
#     if polarity > 0:
#         sentiment = "Positive"
#     elif polarity < 0:
#         sentiment = "Negative"
#     else:
#         sentiment = "Neutral"

#     return sentiment, polarity, subjectivity

# text = input("Enter text to analyze sentiment: ")
# sentiment, polarity, subjectivity = analyze_sentiment(text)
# print(f"Sentiment: {sentiment}")
# print(f"Polarity: {polarity}")
# print(f"Subjectivity: {subjectivity}")

# def isAnagram(s, t):
#     d1={}
#     d2={}
#     if len(s)!=len(t):
#             return False
#     else:
#         for i in range(len(s)):
#             d1[s[i]]=1+d1.get(s[i],0)
#             d2[t[i]]=1+d2.get(t[i],0)
#         for k in d1:
#             if d1[k]!=d2.get(k,0):
#                 return False
#         return True
# s="jar"
# t="jam"
# print(isAnagram(s,t))

# s =input("enter the string: ")
# j=[]
# r=[]
# for i in range(len(s)):
#     if s[i].isalnum():
#         j.append(s[i].lower())
# print(j)
# r=j[::-1]
# print(r)
# if r==j:
#     print(True)
# else:
#     print(False)

#encode

# strs = ["neet", "code", "love", "you"]
# res=""
# for i in strs:
#     res+=str(len(strs))+"#"+i
# print(res)



#decode
s = "4#neet4#code4#love4#you"
res=[]
i=0
for i in range(0,len(s)):
    for j in range(i,len(s)):
        if s[j]!="#":
            j+=1
        length=s[i:j]
        i=j+1
        j=i+int(length)
        res.append(s[i:j])
      
print(res)







# while i<len(s):
#     j=i
#     while s[j]!="#":
#         j+=1
#     length =s[i:j]
#     i=j+1
#     j=i+int(length)
#     res.append(s[i:j])
#     i=j
#     print(res)


