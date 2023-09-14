#map() function
def multiple(n):
    return n*n
num=eval(input("enter any numbers:"))
result=map(multiple,num)
print(list(result))


num1=eval(input("enter any digits:"))
num2=eval(input("enter any digits:"))
result=map(lambda x,y:x+y,num1,num2)
print(list(result))

def double_even (num):
    if num %2==0:
        return num*2
    else:
        return num
numbers=[1,2,3,4]
result=list(map(double_even, numbers))    
print(result)

#nested function
def fun(a,b):
    print(f"sum = {a+b}")
    def sub(a,b):
        print(f"sub= {a-b}")
    sub(a,b)

a=int(input("enter a number 1: "))
b=int(input("enter a number 2: "))
fun(a,b)


def fun2(x,y):
    print(f'highest = {x if x>y else y}')
    def low(x,y):
        print(f'lowest = {x if x<y else y}')
    low(x,y)

x=int(input('enter a number 1: '))
y=int(input('enter a number 2: '))
fun2(x,y)


def function (a,b):
    print(f"multiple={a*b}")
    def division(a,b):
        print(f"division={a%b}")
    division(a,b)
a=int(input("enter any number:"))
b=int(input("enter any number:"))
function(a,b)

