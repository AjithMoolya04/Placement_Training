def create_tuple():
    #creating tuple
    tuple1=(1,2,3,4,5)
    tuple2=("a","b","c","d","e")
    tuple3=("apple","banana","cherry")
    return tuple1,tuple2,tuple3

def access_tupe_items(tuple1,tuple2):
    #accesing the tuple items using positive and negative 
    print("Tuple 1:",tuple1)
    print("First element of the tuple 1:",tuple1[0])
    print("last element of the tuple 1:",tuple1[-1])
    print("tuple 2:",tuple2)
    print("second first element of the tuple 2:",tuple2[1])
    print("second last element of the tuple 2:",tuple2[-2])
    print(tuple[0:5])

def unpacking_tuple1(tuple3):
    #unpacking the tuple
    (green,yellow,red)=tuple3
    print((green))
    print(yellow)
    print(red)
    
def unpacking_tuple2(fruits):
    #unpacking the tuple using asterisk
    fruits=("apple","banana","cherry","straberry","raspberry")
    (green,yellow,*red)=fruits
    print(green)
    print(yellow)
    print(red)
    
def change_tuple(tuple1,tuple2):
    list1=list(tuple1)
    list2=list(tuple2)
    list1.append(6)
    list2.append("c")
    tuple1=tuple(list1)
    tuple2=tuple(list2)
    return tuple1,tuple2

def loop_through_tuple(tuple1):
    print("looping through tuple 1 usinh for loop")
    for i in tuple1:
        print(i)
        
    print("looping through while loop and index number")
    index=0
    while(index<len(tuple1)):
        print(tuple1[index])
        index+=1
        
def join_tuple(tuple1,tuple2):
    #joining tuples 
    tuple3=tuple1+tuple2
    return tuple3     

tuple1,tuple2,tuple3=create_tuple()
access_tupe_items(tuple1,tuple2)
print()

unpacking_tuple1(tuple3)
print()

fruits=("apple","banana","cherry","strawberry","raspberry")
unpacking_tuple2(fruits)
print()

tuple1,tuple2=change_tuple(tuple1,tuple2)
print("After making changes:")
access_tupe_items(tuple1,tuple2)
print()

tuple3=join_tuple(tuple1,tuple2)
print("Joined tuple:",tuple3)  