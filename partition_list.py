#wta to partittion a list arround a given value such that all elelments less than the gievn values come before it and the all element greater then  tha given value come after it
def part(lst,pivot):
    less=[]
    equal=[]
    greater=[]
    for i in lst:
        if i<pivot:
            less.append(i)
        elif(i==pivot):
            equal.append(i)
        else:
            greater.append(i)
    return less+equal+greater
lst=[3,4,1,5,9,2,6,5]
pivot=4
print("partioned list: ",part(lst,pivot))