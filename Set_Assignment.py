# Set:
# 1. Write a program to create an empty set.
# 2. Create a set from a list of elements.
# 3. Write a program, to create new which will contain common elements in two 
# different sets.
# 4. Write a program to get unique items from two sets.
# 5. Update the first set with items that don’t exist in the second set.
# 6. Write a program to return a set of elements present in set a or b, but not both.
# 7. Write a program to check if two sets have any elements in common. If yes, 
# display the common elements.
# 8. Write a program to remove items from set1 that are not common to both set1 
# and set2.
# 9. Write a program to create set of even numbers only.
# 10. Write a program to get size of set.
# 11. Write a program to convert set into tuple and tuple into set.

#Question 1:
s=set()
print(type(s))
print(s)

#Question 2:
l=[1,2,3,4,5]
print(type(l))
s=set(l)
print(type(s))
print(s)

#Question 3:
s1={1,2,3,4,5,6,"vishnu"}
s2={7,8,9,0,"vishnu",5,4}
# s1.intersection_update(s2)
# print(s1)
s3= s1.intersection(s2)
print(s3)

#Question 4:
s1={1,2,3,4,5,6,"vishnu"}
s2={7,8,9,0,"vishnu",5,4}
s3= s1.union(s2)
print(s3)

#Question 5:
s1={1,2,3,4,5,6,"vishnu"}
s2={7,8,9,0,"vishnu",5,4}
s1.update(s2)
print(s1)

#Question 6:
s1={1,2,3,4,5,6,"vishnu"}
s2={7,8,9,0,"vishnu",5,4}
s3= s1.symmetric_difference(s2)
print(s3)

#Question 7:
s1={1,2,3,4,5,6,"vishnu"}
s2={7,8,9,0,"vishnu",5,4}
s3= s1.intersection(s2)
print(s3)

#Question 8:
s1={1,2,3,4,5,6,"vishnu"}
s2={7,8,9,0,"vishnu",5,4}
s3= s1.intersection(s2)
for i in s3:
    s1.remove(i)
print(s1)

#Question 9:
s={1,2,3,4,5,6,7,8,9,10,11}
s1=[]
for i in s:
    if i%2==0:
        s1.append(i)
print(set(s1))

#Question 10:
import sys
s={1,2,3,4,5,6,7,8,9,10,11}
print(sys.getsizeof(s))

#Question 11:
s={1,2,3,4,5,6,7,8,9,10,11}
print(type(s))
print(s)
t=tuple(s)
print(type(t))
print(t)
s1=set(t)
print(type(s))
print(s1)
