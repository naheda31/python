#remove given character in string
word="iam not happy"
print (word.replace("not",""))

print('-----------------------------------')
#check string is palindrome or not
word="level"
if word == word[:: -1]:
    print("the word is pallindrome.")
else:
    print("the word is not pallindrome.")    

print('-----------------------------------')
#to check given character is vowel or consonant
str=input("enter value: ")
if (str=="a"or str=="e"or str=="i"or str=="o"or str=="u"):
   print(str,"is a vowel")
else:
   print(str,"is a consonant")


print('-----------------------------------')

 #to replace string space with given character

s="on the occassion of"
print(s.replace(" ","-"))


print('-----------------------------------')

 #to count alpha,digits and special character
string=("abcd1234@#")
alphabets=0
digits=0
specialchars=0
for i in string:
  if i.isalpha():
       alphabets+=1
  elif i.isdigit():
        digits+=1
  else:
       specialchars+=1
print("alphabet= ",alphabets)
print("digits= ",digits)
print("special characters= ", specialchars )


print('-----------------------------------')


 #to remove all the blank spaces 
word=input("enter value: ")
print(word.replace(" ",""))

print('-----------------------------------')

 # to find sum of integers 

string=input("enter string: ")
digit_sum=sum(int(digit)
    for digit in string
    if digit.isdigit())
print("sum of digits:",digit_sum)

print('-----------------------------------')

 # to remove repeated character
string=input("enter value of string: ")
s=''
for char in string:
    if char not in s:
        s=s+char
        print(s)



print('-----------------------------------')

 #to count the ocurrence of given character
str=("miss universe")
char_count= str.count("s")
print(char_count)

print('-----------------------------------')

 #to check string is anagrams or not
str1=input("enter string:")
str2=input("enter strings: ")
if len(str1)==len(str2):
    print ("string is an anagram")
else:
    print("not an anagram")
