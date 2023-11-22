#Python program to print the highest frequency character in a String.
string="hello world "
dict={}
for char in string:
    if char in dict:
        dict[char] +=1
    else:
        dict[char]=1
max_fe=max(dict.values())
for char in dict:
    if dict[char] == max_fe:
        print(char)
#Python program to Replace First Occurrence Of Vowel With ‘-‘ in String

#  str="python"
# vowels="aeiouAEIOU"
# for i in range(len(str)):
#     if str[i] in vowels:
#         str=str[:i]+"-"+str[i+1:]    
# print(str)


#for all vowels
word="marolix"
vowels="aeiouAEIOU"
result=""
for i in word:
        if i in vowels:
         i="-"
        result += i
print(result)        



#Python program to remove blank space from string.
st="mar olix tech"
re=""
for i in st:
    if i!=" ":
        re +=i
print(re)        


#Python program to concatenate two strings using join() method.
s1="marolix"
s2="technology"
print(''.join([s1,s2]))

#Python program to concatenate two strings without using join() method.
s3=s1+s2
print(s3)


#Python program to remove repeated character from string.
str1="progarmming"
s=""
for char in str1:
    if char not in s:
        s=s+char

print(s)        

#Python program to calculate sum of integers in string.
s4="abdc1234567"
sum=0
for i in s4:
    if i.isdigit():
        sum=sum+int(i)
print(sum)

#Python program to print all non repeating character in string.
s5="hello world"
dt={}
for i in s5:
    if i in dt:
        dt[i]+=1
    else:
        dt[i]=1
non_rep=""
for i in s5:
    if dt[i]==1:
        non_rep += i
print(non_rep)                

#Python program to copy one string to another string.
s6="hello naheda"
s7=""
for char in s6:
        s7 += char
print(s7)        


s8=s6[:]
print(s8)


#Python Program to sort characters of string in ascending order.
string1="python programming"
str_list=list(string1)
ascen_str="".join(sorted(str_list))
print(ascen_str)


#Python Program to sort characters of string in descending  order.

descen_str="".join(sorted(str_list, reverse=True))
print(descen_str)

###Write a program to reverse an integer in Python.

n=123456789
reverse=0
while n!=0:
    reverse=reverse*10+n%10
    n=n//10
print(reverse)   

n1=34567
print(str(n1)[::-1])

#Write a program in Python to check whether an integer is Armstrong number or not
num=123
sum=0
temp=num
count=len(str(num))
while temp>0:
    digit=temp % 10
    sum+=digit **count
    temp //=10
if num==sum:
    print("armstrong number")
else:
    print("not an armstrong number")        
    

#Write a program in Python to check given number is prime or not.
n2=3
i,temp=0,0
for i in range(2,n2//2):
    if n2 % i==0:
        temp=1
if temp==1:
    print("not a prime ")    
else:
    print("prime ")    



