#Question 1:
ch1 =  "Name"
ch2 = "Is"
ch3 = "Vishnu Akash"
print(ch1+"**"+ch2+"**"+ch3)
print(ch1+ch2+ch3)
print('Name', 'Is', 'James', sep='**')

#Question 2:
a = int(input())
b = int(input())
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)

#Question 3:
num = 9
print('%o'%num)

#Question 4:
num = 5.7777
print('%.2f'%num)

#Question 5:
name = "Vishnu Akash"
age = "twenty four"
city = "Namakkal"
print(name,age,city)

#Question 6:
Name  = "my name is vishnu akash"
print(Name.upper())

#Question 7:
Name = "My name is Vishnu Akash"
print(len(Name))
temp = 0
for i in Name:
    temp += 1
print(temp)

#Question 8:
Name = "My name is Vishnu Akash"
for i in range(len(Name)):
    if i%2==0:
        print(Name[i],end='')

#Question 9:
import math
r = int(input())
a = math.pi*r*r
print(a)

#Question 10:
word  = "my name is vishnu akash"
words = word.split()
output = list(reversed(word))
print("".join(output))
##########
word  = "my name is vishnu akash"
ch = word[::-1]
print(ch)

#Question 11:
txt = "madam"
if txt == txt[::-1]:
    print("Palindrome")
else:
    print("Not Palidrome")

#Question 12:
txt = "Vishnu Akash"
for i in txt:
    ascii = ord(i)
    print(i,"\t",ascii)

#Question 13:
num = int(input())
ascii = chr(num)
print(num,"\t",ascii)

#Question 14:
word  = input().split()
count = 0
for i in range(len(word)):
    count +=1
print(count)

#Question 15:
input_string = input()
txt = input_string.lstrip().rstrip()
print("my name is",txt,"i am from namakkal")       

#Question 16:
input_num = input()
print(input_num[::-1])

#Question 17:
std1 = "BAT"
std2 = "GIT"
l=[]
output = ''
x = list(zip(std1,std2))
for i in x:
    l.append(''.join(i))
    output=(''.join(l))
print(output)

#Question 18:
st = input()
temp = 0
for i in st:
    if i=='a' or i=='e' or i=='o' or i=='u' or i=='1':
        temp = temp + 1
print(temp)

#Question 19:
st = input()
l=[]
for i in st:
    if i.isalpha():
        l.append(i)
print(''.join(l))

#Question 20:
st1 = "Vishnu"
st2 = "Vishnu"
if st1 == st2:
    print("same")
else:
    print("Not same")

#Question 21:
st = "Vishnu"
print(len(st))