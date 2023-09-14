#recursive function
def recur_factor(n,a=1):
    if (n==0):
        return a
    return recur_factor(n-1,n*a)
print(recur_factor(5))

def sum(list):
    sum=0
    for i in range(len(list)):
        sum=sum+list[i]
    return sum
print(sum([1,2,3,4,5]))

def factorial(y): 
    if y==1:
        return 1
    else:
        return y * factorial(y-1)  
print(factorial(100))

#lambda function
x=lambda a,b:a**b
print(f'square of x is {x(2,3)}')


a=lambda n:n+n
print(a(5))

s=lambda num:num*5
print(s(5))


#filter()function
def check(letter):
    list_of_vowels=['a','e','i','o','u']
    if letter in list_of_vowels:
        return True
    else:
        return False
letters=['a','b','c','d','e','f','g','h']
filter_object=filter(check,letters)
print(list(filter_object))

def isodd(num):
    return num%2 !=0

numbers=[1,2,3,4,5,6,7,8,9]
odd_list=list(filter(isodd, numbers))
print(odd_list)


def iseven(num):
    return num%2 ==0

numbers=[1,2,3,4,5,6,7,8,9]
even_list=list(filter(iseven, numbers))
print(even_list)

