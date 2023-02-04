# Tuple:
# 1. Create tuple of numbers 1 to 10.
# 2. Create single value tuple.
# 3. Create one number element tuple and square all the elements in that tuple and 
# store in new list.
# 4. Write a Python program to create a tuple.
# 5. Write a Python program to create a tuple with different data types.
# 6. Write a Python program to create a tuple of numbers and print 2nd item.
# 7. Write a Python program to unpack a tuple into several variables.
# 8. Write a Python program to add an item to a tuple.
# 9. Write a Python program to convert a list to a tuple.
# 10. Write a Python program to find the length of a tuple without using len function.
# 11. Write a Python program to reverse a tuple.
# 12. Write a Python program to convert a list of tuples into a dictionary.
# 13. Write a Python program to calculate the product, multiplying all the numbers in a 
# given tuple.
# 14. Write a Python program to calculate the average value of the numbers in a given 
# tuple.
# 15. Write a Python program to convert a tuple of string values to a tuple of integer 
# values.
# 16. Write a Python program to convert a given list of tuples to a list of lists.
# 17. Write a python program to get size of tuple.
# 18. Create one and list and one tuple with same elements and compare their sizes.
# 19. Get count a particular element in tuple.
# 20. Write a Python program to get the 4th element and 4th element from last of a tuple.

#Question 1:
t=[]
for i in range(20):
    t.append(i)
print(tuple(t))

#Question 2:
t=555,
print(type(t))
print(t)

#Question 3:
t=(1,2,3,4,5,6,7,8,9)
tp=[]
for i in t:
    tp.append(i*i)
print(tp)

#Question 4:
t=tuple(range(1,11))
print(type(t))
print(t)

#Question 5:
l=[1,2,3,4,5,6,7]
t=tuple(l)
print(t)
s="vishnu","john","navin","jeeva","sekar"
print(type(s))
print(tuple(s))
t=(1,2,"vishnu",8.0,True)
print(tuple(t))

#Question 6:
t=(1,2,3,4,5,6,7)
print(t[1])
t=tuple(range(1,11))
print(t[1])

#Question 7:
t=(1,2,3,4,5,6,7)
(t1,t2,t3,t4,*t5)=t
print(t1,t2,t3,t4,*t5)

#Question 8:
t=("vishnu","navin","john")
l=list(t)
l.append("jeeva")
print(tuple(l))

#Question 9:
l=[1,2,3,4,5]
t=tuple(l)
print(t)

#Question 10:
t=("vishnu","navin","john",1,3,4,5)
print(type(t))
c=0
for _ in t:
    c+=1
print(c)

#Question 11:
t=("vishnu","navin","john",1,3,4,5)
tmp=list(t)
tmp.reverse()
print(tmp)

#Question 12:
t=[("A","vishnu"),("B","navin"),("c","john"),("D","Jeeva")]
tmp=dict(t)
print(tmp)

#Question 13:
t=(1,2,3,4,5)
tmp=1
for i in t:
    tmp=tmp*i
print(tmp)

#Question 14:
t=(1,2,3,4,5)
tmp=sum(t)
print(tmp)
print(tmp/len(t))


#Question 15:
t=("1","2","3","4","5")
tmp=tuple(map(int,t))
print(tmp)
# tmp1=[]
# for i in t:
#     tmp1.append(int(i))    
# print(tuple(tmp1))

#Question 16:
t=[("A","vishnu"),("B","navin"),("c","john"),("D","Jeeva")]
t1=list(map(list,t))
print(t1)
# tmp=[]
# for i in t:
#     tmp.append(list(i))
# print(tmp)

#Question 17:
import sys
t=(1,2,3,4,5)
print(sys.getsizeof(t))
t2 = ("Vishnu", "Navin", "Jeeva", "Dharani", "John", "Akash")
print(t2.__sizeof__())

#Question 18:
l=[1,2,3,4,5,6,7,8,9,10]
t=("Vishnu", "Navin", "Jeeva", "Dharani", "John", "Akash")
print(l.__sizeof__())
print(t.__sizeof__())

#Question 19:
t=("Vishnu", "Navin", "Jeeva", "Dharani", "John", "Akash")
for i in t:
    print("{} : {}".format(i,t.count(i)))
    
#Question 20:
t=("Vishnu", "Navin", "Jeeva", "Dharani", "John", "Akash")
tmp=len(t)-1
print(t[4])
print(t[tmp-3])