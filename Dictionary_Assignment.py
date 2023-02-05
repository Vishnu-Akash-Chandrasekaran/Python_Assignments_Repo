# Dictionary:
# 1. Create an empty dictionary then add some key value pairs, like 
# name,age,address..etc.
# 2. Take two lists of same size and make first list members as key and second list 
# elements as values.
# 3. Take one lists of duplicate numbers, and make a dictionary which key is list element 
# and value is number of occurrences of that element in that list. 
# 4. Write a Python script to add a key to a dictionary.
# 5. Write a Python program to iterate over dictionaries using for loops.
# 6. Write a program to sum values in that dictionary.
# 7. Write a Python program to sort a given dictionary by key.
# 8. Write a Python program to sort a given dictionary by values.
# 9. Write a Python program to get the maximum and minimum values of a dictionary.
# 10. Write a Python program to get total number of items in that dictionary.
# 11. Write a Python program to replace values of dictionary with sum of key and value.
# 12. Write a Python program, take on list of words and create new dictionary its words 
# are keys of that dictionary and values as length of the word.
# 13. Write a Python program to invert key, value pairs in dictionary.
# 14. Write a Python program, take one numbers list and create new dictionary its key is 
# number and value is square of that number from numbers list.
# 15. Merge two dictionaries into one dictionary.

#dictionary_name = {key: value}
#Question 1:
d={}
for i in range(2):
    d[input("enter key: ")]=input("enter value: ")
print(d)

#Question 2:
l1=[1,2,3,4,5,]
l2=["a","b","c","d","f"]
d={}
# l=dict(zip(l1,l2))
# print(l)
for x,y in zip(l1,l2):
    d[x]=y
print(d)

#Question 3:
l1=[1,2,3,4,5,5,3,2,1,5,5,5]
l2=set(l1)
d={}
for i in l2:
    d[i]=l1.count(i)
print(d)

#Question 4:
d={}
for i in range(3):
    d[input("enter key :")]=''
print(d)

#Question 5:
d={"name":"vishnu","age":24,"city":"namakkal"}
for x,y in d.items():
    print(x,y)

#Question 6:
d={"a":1,"b":2,"c":3,"d":4,"e":5}
tmp=0
for x in d.values():
    tmp = tmp+x
print(tmp)

#Question 7:
d={"c":1,"b":2,"a":3,"e":4,"d":5}
l=[]
for x,y in d.items():
    l.append([x,y])
l.sort()
print(dict(l))

#Question 8:
d={"c":2,"b":4,"a":1,"e":5,"d":3}
l=[]
for x,y in d.items():
    l.append([y,x])
l.sort()
print(dict(l))

#Question 9:
d={"c":2,"b":4,"a":1,"e":5,"d":3}
print(max(d.items()))
print(min(d.items()))

#Question 10:
d={"c":2,"b":4,"a":1,"e":5,"d":3}
print(len(d))
tmp=0
for x in d.values():
    tmp=tmp+x
print(tmp)

#Question 11:
d={2:25,1:10,3:5,4:11,5:100}
for x,y in d.items():
    tmp = x+y
    d[x]=tmp
print(d)

#Question 12:
l=["vishnu","john","navin","jeeva","sekar"]
d={}
for i in l:
    tmp=len(i)
    d[i]=tmp
print(d)

#Question 13:
d={1:"vishnu",2:"john",3:"navin",4:"jeeva",5:"sekar"}
tmp={}
for x,y in d.items():
    tmp[y]=x
print(tmp)

#Question 14:
l=[1,2,3,4,5,6,7,8,9,10]
d={}
for i in l:
    d[i]=i*i
print(d)

#Question 15:
d1={"a":1,"b":2,"c":3,"d":4,"e":5}
d2={"name":"vishnu","age":24,"city":"namakkal"}
d1.update(d2)
print(d1)

#Question 16:
d={"a":1,"b":2,"c":3,"d":4,"e":5}
tmp = 0
for x in d.values():
    tmp=tmp+x
print(tmp)

#Question 17:
d={"a":1,"b":2,"c":3,"d":4,"e":5}
tmp = list(zip(d.keys(),d.values()))
print(tmp)

#Question 18:
import sys
d={"name":"vishnu","age":24,"city":"namakkal"}
print(sys.getsizeof(d))

#Question 19:
d={"name":"vishnu","age":24,"city":"namakkal"}
d["city"]="tamilnadu"
print(d)

#Question 20:
d={}
for i in range(3):
    d[input("enter key: ")]=input("enter value: ")
print(d)

d={"name":"","age":'',"city":""}
for x,y in d.items():
    print(f"enter {x} :",end='')
    d[x]=input()
print(d)