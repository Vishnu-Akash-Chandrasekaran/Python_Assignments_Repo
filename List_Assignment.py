# Lists:
# 1. Create a list of only even numbers.
# 2. Create one list of 1 to 10 numbers and create new list which contain square of the 
# numbers from this number list.
# 3. Take three input numbers from the user and create list from those numbers.
# 4. Take one list of numbers and do sum of all numbers in that list without using sum 
# function.
# 5. list_one = [1,2,3,4], list_two =[1,2,3,4], check that these two lists content is same of 
# not.
# 6. list_one = [1,2,3,4], list_two =[1,2,3,4], check that these two lists 
# addresses/references are same of not.
# 7. list1 = [100,200,100,400,500,300], reverse this list.
# 8. Reverse above list without using reverse function.
# 9. Reverse the above lists using slicing.
# 10. Concatenate two list index wise,
# Eg.l1 = [‘A’,’B’,’C’]
# l2 = [‘X’,’Y,’Z’]
# o/p: [‘AX’,’BY’,’CZ’]
# 11. Create one list of numbers from 1 to 10 and extract only last 5 numbers from that 
# list.
# 12. Take a list of names and convert those all names into Upper case words.
# 13. Take list of names and count number of characters in each name and print on the 
# console, name and its length.
# 14. Create one list of elements and take specific element and position of element from 
# user and add that element at that position.
# 15. Take list of numbers and print on the console element and number of occurrences of 
# that element in that list.
# 16. Check the start and end element of the lists are same or not.
# 17. Take the list of strings and sort in both ascending and descending order.
# 18. Take a number list and calculate sum and average of list elements.
# 19. Take a number list and count even and odd numbers in that list.
# 20. Reverse a list without using inbuilt function.
# 21. Get only unique elements from the list.
# 22. Take two lists with same number of elements and subtract elements from one list 
# from other list element and create new list for that subtraction result.
# 23. Take one list elements and create two separate lists those contain odd numbers and 
# even numbers separately.
# 24. Take a list of numbers in the string format, convert those numbers into integer 
# format and get sum of all those list elements.

#Question 1:
lst = int(input("Enter the number for an end: "))
l = []
for i in range(lst):
    if i%2==0:
        l.append(i)
print(l)

#Question 2:
lst = [1,2,3,4,5,6,7,8,9,10]
l = []
for _ in range(lst):
    l.append(i*i)
print(l)

#Question 3:
l1 = int(input("Enter the number: "))
temp1=[]
l2 = int(input("Enter the number: "))
temp2=[]
l3 = int(input("Enter the number: "))
temp3=[]
for x in range(l1):
    temp1.append(x)
print(temp1)
for x in range(l2):
    temp2.append(x)
print(temp2)
for x in range(l3):
    temp3.append(x)
print(temp3)

#Question 4:
lst = int(input())
temp=0
#[1,2,3,4,5,6,7,8,9]
for i in range(lst):
    temp=temp+i
print(temp)

#Question 5:
l1=[1,2,3,4,5]
l2=[1,2,3,4,5,456]
if l1==l2:
    print("Same")
else:
    print("Not Same")

#Question 6:
l1=[1,2,3,4,5]
l2=[1,2,3,4,5,456]
print(id(l1))
print(id(l2))
if id(l1)==id(l2):
    print("Same")
else:
    print("Not Same")

#Question 7:
l1=[100,200,100,400,500,300]
l1.reverse()
print (l1)

#Question 8:
l1=[100,200,100,400,500,300]
temp=[]
for _ in range(1,len(l1)+1):
    temp.append(l1[-_])
print(temp)

#Question 9:
l1=[100,200,100,400,500,300]
print(l1[::-1])

#Question 10:
l1=["a","b","c"]
l2=["x","y","z"]
temp1=[x+str(y) for x,y in zip(l1,l2)]
print(temp1)

#Question 11:
l=[1,2,3,4,5,6,7,8,9,10]
print(l[5::])
# temp=[]
# for i in l[:len(l)-6:-1]:
#     temp.append(i)
# print(temp)

#Question 12:
l=["vishnu","john","navin","jeeva","sekar"]
temp=[]
for i in l:
    s = i.upper()
    temp.append(s)
print(temp)

#Question 13:
l=["vishnu","john","navin","jeeva","sekar"]
# d=[]
# op={}
# for i in l:
#     i.split()
#     op[i]=len(i)
# print(op)

for i in l:
    print("{}:{}".format(i,len(i)))

#Question 14:
l=["vishnu","john","navin","jeeva","sekar"]
ele = input()
num =int(input())
l.insert(num,ele)
print(l)

#Question 15:
l=[1,2,3,4,5,6,7,8,9,2,3,5,6,6,6,2,7,7,8,8,9,9,4,4]
temp=set(l)
for i in temp:
    print(i,l.count(i))

#Question 16:
l=["vishnu","john","navin","jeeva","sekar","nanba"]
if l[0] == l[-1]:
    print("Same")
else:
    print("Not Same")

#Question 17:
l=["vishnu","john","navin","jeeva","sekar","nanba"]
l.sort()
print(l)
l.sort(reverse=True)
print(l)

#Question 18:
l=[1,2,3,4,5,6,7,8,9]
temp = sum(l)
print(temp)
print(temp/len(l))

#Question 19:
l=[1,2,3,4,5,6,7,8,9,11]
c1=0
c2=0
for i in l:
    if i%2==0:
        c1+=1
    if i%2!=0:
        c2+=1
print("Even: ",c1)
print("Odd: ",c2)

#Question 20:
l=[1,2,3,4,5,6,7,8,9,10]
temp=[]
for _ in range(1,len(l)+1):
    temp.append(l[-_])
print(temp)

#Question 21:
l=[1,2,3,4,5,6,7,8,9,10,10]
t=[]
for i in l:
    if l.count(i)==1:
        t.append(i)
print(t)

#Question 22:
l=[1,2,3,4,5]
l1=[9,25,10,9,15]
temp1=[]
for x,y in zip(l,l1):
    temp = y-x
    temp1.append(temp)
print(temp1)

#Question 23:
l=[1,2,3,4,5,6,7,8,9,10]
t1=[]
t2=[]
for i in l:
    if i%2==0:
        t1.append(i)
    if i%2!=0:
        t2.append(i)
print(t1)
print(t2)

#Question 24:
l=['1','2','3','4','5','6','7','8','9','10']
l1=list(map(int,l))
print(sum(l1))    
# temp=[]
# for i in l:
#     temp.append(int(i))
# print(sum(temp))