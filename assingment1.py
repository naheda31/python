#membership operators .
str1="naheda"
str2="nafisa"
print(str1 in str2) 
print(str1 not in str2)
print(str2 in str1)

s1="a b c"
s2="b b d"
print (s1 not in s2)
print (s2 in s1)

s1="iam beautiful"
s2="your beautiful"
print(s1 not in s2)
print (s2 in s1)

print("-------------")
#removing spaces by using strip
string= "  python is easy to learn  "
print(len(string))
after_strip = string.strip()
print(after_strip)
print(len(after_strip))

s1="    iam an indian"
print(len(s1))
after_strip=s1.lstrip()
print(after_strip)
print(len(after_strip))

word="chandrayan landed on moon    "
print(len(word))
after_strip=word.rstrip()
print(after_strip)
print(len(after_strip))

print('-------------')
#comparing 2 strings
a="aeroplane"
b= "helicopter"
print(a<b)
print(b<a)

s1="ab bc cd"
s2="bc cd de"
if s1== s2:
      print("both s1 and s2 are same")
else :   print("diffrent strings")

a="$naheda"
b="@mohammad"
print(a==b)
print(b>=a)

print('----------')

#finding substring by using index
str="chandrayan landed on moon"
print(str.index('moon'))

s1="earth is a planet"
print(s1.index("is"))

s1= 'iam beautiful'
print(s1.index("a"))

print('------------')
#rindex

str="chandrayan landed on moon"
print(str.rindex("moon"))

s1="earth is a planet"
print(s1.rindex("is"))

print("----------------")

#finding string using find of
string="my name is naheda"
print(string.find("n"))


s1="iam learing python"
print(s1.find("in"))

string="my name is naheda"
print(string.find('n',9,15))

#rfind .....
string="iam an indian"
print(string.rfind("i"))

word="apple is good for health"
print(word.rfind("o"))
print(len("for"))

#replace
word="iam a bad human "
print(word.replace("bad","good"))

s1="if ur bad iam bad"
print(s1.replace("bad","good"))

s="iam not happy"
print(s.replace("not","so"))

print('---------------')

#split of

text="apple@banana@mango"
s=text.split("@")
print(s)


string="hello,iam naheda,and am working at ,marolix technology"
print(string.split(","))


print("-------------")
#joining

list=["apple","banana","mango"]
s=":".join(list)
print(s)

tuple=("apple","banana","mango")
s="#".join(tuple)
print(s)
