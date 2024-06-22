id = input("Enter the mail id: ")
name=''
d=0
for i in id:
    if i =="@":
        break
    else:
        name=name+i
        
gmail=0
if id.endswith("@gmail.com"):
    gmail=1
    
for j in name:
    if name[0].isdigit():
        d=0  
    if j.islower() or j.isdigit():
        d=1   
    else:
        d =0
        break
        
        
if gmail==1 and d ==1:
    print("valid mail id")
else:
    print("Invalid mail id")