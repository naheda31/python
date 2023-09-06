#1.Write a Python script to add a key to a dictionary
d={0:10,1:20}
if 2 not in d:
    d[2]=30
print(d)    

print("-----------------------------------")
#2.Write a Python script to check whether a given key already exists in a dictionary
dict={"product name":"chocolate","price":100,"company":"dairy milk"}
print(dict["product name"])


print("-----------------------------------")
#3.Write a Python program to iterate over dictionaries using for loops
dt={'a':"apple","b":"banana","c":"cat","d":"dog"}
for key in dt.keys():
    print(key)
for value in dt.values():
    print(value)  


print("-----------------------------------")
#4.Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys
dt={}
for i in range(1,16):
    dt[i]=i**2
print(dt) 
   
print("-----------------------------------")

#5.Write a Python program to create a dictionary from a string.
string="marolix technology"
letter_count={}
for char in string:
    if char in letter_count:
        letter_count[char]+=1
    else:
        letter_count[char]=1
print(letter_count)            


print("-----------------------------------")

#6.Write a Python program to sum all the items in a dictionary
my_dict={'apple':100,'banana':200,'mango':300}
print(sum(my_dict.values()))  

print("-----------------------------------")
#7.Write a Python program to combine two dictionary by adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
for key in d2:
    if key in d1:
        d2[key]=d1[key]+d2[key]
print(d2)        

print("-----------------------------------")

#8.Write a Python program to access dictionary key's element by index.
dict={'physics':90,'math':100,'chemistry':90}
print(dict.keys())
for i in dict:
    print(i)

print("-----------------------------------")

#9.Write a Python program to remove a key from a dictionary   
dt['name']=["naheda"]
dt["surname"]=['mohammad']
dt['domain']=['python']
dt['empid']=[100]
print(dt.pop("surname"))
print(dt)

print("-----------------------------------")
#10.Write a Python script to merge two Python dictionaries.d
dt1={"a":100,"b":200,"c":300}
dt2={1:"a",2:"b",3:"c"}
dt3=dt2.copy()
dt3.update(dt1)
print(dt3)
 