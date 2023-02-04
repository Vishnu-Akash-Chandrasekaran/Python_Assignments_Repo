# String:
# 1. Display three strings ‘Name’,’Is’ ,’James’ as ‘ Name**Is**James’.
# 2. Accept two numbers input from user, and do mathematical operations, (addition,
# subtraction, multiplication, division, modulo division, floor division).
# 3. Convert decimal number into octal number using , format specifier in print function.
# 4. Display float number with two decimal places, using print function.
# 5. Take three different strings from input and assign to three different variables and 
# display on the console.
# 6. Take a input string and convert each character into upper case.
# 7. Take input string and calculate its length without using len function.
# 8. Take input string and extract only even position characters.
# 9. Take circle radius input from user and calculate area of a circle.
# 10. Reverse a string by its words.
# 11. Take input string from user and check that is entered string is palindrome or not.
# 12. Take one input string and find ASCII value of each character and print on the console 
# with that character.
# 13. Ask user to enter number from 0 to 255 and print on the console its corresponding 
# character.
# 14. Get word count , from paragraph.
# 15. Take input string from user, while entering string if user gives spaces at starting or 
# ending of the string, remove those spaces and print string on the console.
# 16. Reverse the entered 4-digit number. Eg. input is 1804, o/p should be: 4081.
# 17. Take two string and add alphabets alternatively and form single string.eg.st1 = “BAT” 
# ,st2=”GIT”, then output should be: BGAITT.
# 18. Count number of vowels in the string.
# 19. Remove any special symbol, numbers from the list, keep only alphabets.
# 20. Take two input strings from the user and check are those strings same or not.
# 21. Write a program to get size of string.

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