#python program to remove given character from string
s=input("enter the string:")
s1=input("enter the character which you want to remove: ")
s2=s.replace(s1,"")
print(s2)

def remove_char(s,s1):
 print(s.replace(s1,""))

s=input("enter the string:")
s1=input("enter the character which you want to remove: ")
remove_char(s,s1)


#python program to count the occurence of the given string
s="my name is naheda and my age is 22yrs "
print(s.count("my"))
print(s.count("my",0,5))

char="n"
count=0
for i in range(len(s)):
    if (s[i]==char):
        count=count+1
print("total no.of",char,"is",count)

#python program if two strings are anagram or not
str1="listen"
str2="silent"
if sorted(str1)==sorted(str2):
    print("anagram")
else:
    print("not an anagram")    

#python program to check the string is pallindrome or not
st="mom"
if st[::-1]==st:
    print("is a pallindrome")
else:
    print("not a pallindrome")   

#python program to check whether the given character is a vowel or consonant
vowel=['a,e,i,o,u']
string="z"
for i in string:
    if i  in vowel:
        print("is a vowel")
    else:
        print("is a consonant")    


# python program to check the given character is digit or alpha
char=1
if char>=0 or char <=9 :
    print("given char is a digit")
else:
    print("is a alphabet")    

#python program to check the given character is digit or not using isdigit
ch="a"
if (ch.isdigit()):
    print("given ch is a digit")
else:
    print("not a digit")


#Python program to replace the string space with a given character.
str3="marolix technology"
result=""
char1="@"
for i in str3:
         if i == " ":
          i = char1
         result += i
print(result)        


#Python program to replace the string space with a given character using replace()

print(str3.replace(" ","@"))


#Python program to convert lowercase char to uppercase of string.
word="marolix"
reslt=''
for i in word:
    if i.islower():
        i=i.upper()
        reslt += i
print(reslt)        

#upper to lower
found=""
for i in reslt:
    if i.isupper():
        i=i.lower()
        found += i
print(found)        


#Python program to convert lowercase vowel to uppercase in string

word="marolix"
vowels="aeiou"
for char in word:
    if char in vowels:
        upper_char = char.upper()
        word =word.replace(char, upper_char)
print(word)


#Python program to delete vowels in a given string.
word1="website"
result1=""
for i in word1:
        if i in vowels:
         i=""
        result1 += i
print(result1) 


#Python program to count the Occurrence Of Vowels & Consonants in a String
word2="naheda"
vowel =0
consonant=0
for i in word2:
    if i in ('a','e','i','o','u'):
        vowel +=1
    else:
        consonant +=1
print("vowels: ", vowel , "consonant: ", consonant)        


#Python program to print the highest frequency character in a String.

#Python program to Replace First Occurrence Of Vowel With ‘-‘ in String

#Python program to count alphabets, digits and special characters.
word3="abcd123@#"
alphbates=0
digits=0
special=0
for i in word3:
    if i.isalpha():
        alphbates+=1
    elif i.isdigit():
        digits+=1
    else:
        special +=1
print("alphabates:",alphbates,"digits:",digits,"special:",special)      

#Python program to separate characters in a given string.
string1="hello naheda"
for i in string1:
    print(i)

s1="\n".join(list(string1))    
print(s1)


