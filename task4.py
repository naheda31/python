employe_details=[]
def add():
    global employe_details
l=int(input("enter no.of employe details to enter:"))    
for i in range(1,l+1): 
   dict={}  
domain=input("enter a domain name:")
name=input("enter a employee name:")
emp_id=input("enter a empid:")
email_id=input("enter a emailid:")
employe_details.append(dict)

def prnt():
    global employe_details
    l=input("to print a employe details type a,to get all employee details type b: ")
if l=="a":
    chr=input("enter any details of employe:")
    for i in employe_details:
     if chr==i.get("domain")or chr==i.get("name") or (chr== i.get("emp_id") or chr == i.get("email_id")):
        print(i)
        break
    else:
       print("employee details not found")  
    
elif  l =='b':
   print(employe_details)
   

def get_details():
   l=input("to add an employe type add or to print details type print:")  
   if l=="add":
      add()
   elif l=="print":
      print()
get_details()