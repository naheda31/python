#Write a program in Python to print the Fibonacci series using iterative method.
               # a series in which next number is the sum of previous two numbers
n=5
first,second=0,1
print("fibnacci series:")
for i in range(0,n):
    if i <=1:
        result=i
    else:
        result=first+second
        first=second
        second=result
    print(result)

#Write a program in Python to print the Fibonacci series using recursive method.
num=7
first,second=0,1
def fibonacci (num):
    if num == 0:
        return 0
    elif num ==1:
        return 1
    else:
        return fibonacci(num -1) + fibonacci(num -2)
print("fibnacci of given number is:")
for i in range(0,num):
    print(fibonacci(i))    

#Python program for palindrome using an iterative method
n1=121
reverse=0
temp=n1
while temp!=0:
     reverse=reverse*10 + temp % 10
     temp=temp//10
if reverse==n1:
    print("is a pallindrome") 
else:
    print("not a pallindrome")    

#Write a program in Python to find sum of digits of a number using recursion
num=12345
def find_sum(num):
    if num== 0:
        return 0
    else:
        return int(num %10) + find_sum(num/10 )
print(find_sum(num))    


#Python Program to find the Average of numbers 
numbers=[30,40,50,60]
average=sum(numbers)/len(numbers)
print(average)


#Python Program to calculate factorial using iterative method.
number=5
factorial=1
if number <0:
    print("factorail cannot be done for negative numbers")
elif number==0:
    print("factorial of 0 is 1")
else:
 for i in range(1,number+1):
  factorial = factorial*i
print(factorial)

#Python Program to calculate factorial using recursion.
def factorial(x):
    if x==1:
        return x
    else:
        return x*factorial(x-1)
    
print(factorial(10))   

#Python Program to check a given number is even or odd.

num=24
if num%2==0:
    print("is even ")
else:
    print("not an even")


#Python program to find greatest of three numbers
n1=12
n2=6
n3=25
if n1>=n2 and n1>=n3:
    print("n1 is greater")
if n2>=n1 and n2>=n3:
    print("n2 is greater")
if n3>=n1 and n3>=n2:
    print("n3 is greater")

#Python Program to find Smallest number among three.
n1=12
n2=6
n3=25
if n1<=n2 and n1<=n3:
    print("n1 is smallest")
if n2<=n1 and n2<=n3:
    print("n2 is smallest")
if n3<=n1 and n3<=n2:
    print("n3 is smallest")

#Swapping of two numbers using third variable 
a=123
b=456
c=a
a=b
b=c
print(a)
print(b)
    
#Add two number without + Operator in Python
def add_num(x,y):
    while y !=0:
        temp= x&y
        x=x^y
        y=temp >> 1
        return x
num1=10
num2=20
print(add_num(num1,num2))   

#Python Program to calculate the power using ‘pow()’ method
numbr=5
exponent=4
print(pow(numbr,exponent))


#Python Program to calculate the square of a given number
print(num*num)

#Python program to calculate the cube of a given number
print(num*num*num)


#Python program to calculate the square root of a given number
from math import *
print((sqrt(num)))






