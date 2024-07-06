import collections 
s= ["act","pots","tops","cat","stop","hat"]
d=collections.defaultdict(list)  #creating a default list which store the keys and values

for i in s:  
    count=[0]*26   #creating an list of  26s [0,0,0,0,0,0,0,0,0,0,0,00,0,0,0,00,0,0,0,0,0,0]
    for c in i:
        count[ord(c)-ord('b')]+=1  # here we are using a aasscii values for geting the key updating o to 1 
    d[tuple(count)].append(i)  #converting the keyy as a tupple 
print(d.values())
