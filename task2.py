#1.write a python program 
l1=eval(input("enter any element: "))
l2=eval(input("enter any element: "))
l3=l1+l2
print(l3)

print("-----------------------------------------")
#2.write a python program to find the sum of list elements
lst1=eval(input("enter numbers:"))
total=0
for num in lst1:
    total+=num
    print("the sum of elements in the list :",total)

print("-----------------------------------------")

#3.write a python program to print even and odd numbers seperatly in list
lst=eval(input("enter values:"))
even_number=[]
odd_number=[]
for number in lst:
    if number %2==0:
       even_number.append(number)
    else:
        odd_number.append(number)
print ("even numbers:",even_number)     
print("odd number",odd_number)


print("-----------------------------------------")


#4.write a python program to delete element of given index in list.
l1=list(eval(input( "enter any number is seperated by comma(,)in single line:")))
index=eval(input("enter index position:"))
l1.pop(index)
print(l1)


print("-----------------------------------------")


#5.write a python program to delete given elemet from the list
l1=list(eval(input( "enter any number is seperated by comma(,)in single line:")))
given_element=eval(input( "enter any number:"))
l1.remove(given_element)
print(l1)



print("-----------------------------------------")


#6.write a python program to insert an elemet  at given index location
l1=list(eval(input( "enter any number is seperated by comma(,)in single line:")))
insert=eval(input("enter any number:"))
element=eval(input("enter the element:"))
l1.insert(insert,element)
print(l1)
print("-----------------------------------------")


#7.write a python program to check the sizes of given two lists are same.
l1=list(eval(input('enter a group of elements separated by comma(,) in a single line: ')))
l2=list(eval(input('enter a group of elements separated by comma(,) in a single line: ')))
if (len(l1) == len(l2)):
    print(' both the lists are same')
else:
    print('both the lists are diffrent')


print("-----------------------------------------")

#8.Write a Python program to remove a specified column from a given nested list.
l=[[1, 2, 3], [2, 4, 5], [1, 1, 1]]
l1=[]
for i in range(int(len(l))):
    value=l[i]
    value.pop(0)
    l1.append(value)
print(l1)


print("-----------------------------------------")


#9. Write a Python program to convert a list of multiple integers into a single integer
l=list(eval(input('enter a group of elements separated by comma(,) in a single line: ')))
l1=''
for i in l:
    l1+=str(i)
print(l1)



print("-----------------------------------------")


#10.Write a Python program to remove duplicates from a list.
l1=list(set(eval(input('enter a group of elements separated by comma(,) in a single line: '))))
print(l1)

