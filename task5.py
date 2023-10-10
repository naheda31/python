# wite a python program to create calculator.
def add(x,y):
   return(x+y)
def subtract(x,y):
   return(x-y)
def multiple(x,y):
   return(x*y)
def division (x,y):
   return(x/y)
print("select the operator:")
print("1.add")
print("2.subtract")
print("3.multiple")
print("4.division")

operator=input("enter the operator which you need 1/2/3/4:")
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))

if operator=="1":
    print(num1,"+", num2, "=" ,add(num1,num2))
elif operator=="2":
    print(num1,"-",num2,"=",subtract(num1,num2))
elif operator=="3":
    print(num1,"*",num2,"=",multiple(num1,num2))    
elif operator=="4":
    print(num1,"/",num2,"=",division(num1,num2))    
else:
    print("invalid details")    


# write a program to enter employee details and also filter the stored employee details with name,empid,designation and email.
employee_list=[]
def employee_details():
    employee={}
    employee["name"]=input("enter any name:")
    employee['empid']=input("enter any id:")
    employee["designation"]=input("enter a designation:")
    employee['email']=input("enter a emailid:")
    employee_list.append(employee)  
    print("details added sucessfully")   
def filter_employee():
    fliter=input("enter the filter which you need: ")
    for d in employee_list:
     if d.get('Name') == fliter :
       print(d)
            
     elif d.get('Empid') == fliter :
          print(d)
            
     elif d.get('Email') == fliter :
           print(d)
            
     elif d.get('Designation') == fliter :
           print(d)
     else:
          print('employee with the given filter is not found')  

while True:
    n=input('To add employee type a, To filter type f: ')
    if n == "a":
        employee_details()
    elif n == "f" :
        filter_employee()