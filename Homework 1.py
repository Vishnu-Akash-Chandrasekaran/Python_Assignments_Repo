# input
name = input()
age = input()
print(name,age)

# Format specifier
print ("Hello, My name is %s and I am %s years old."%(name,age))

# Format method
name = input()
age = input()
print("Hello, My name is {} and I am {} years old.".format(name,age))
print("Hello, My name is {1} and I am {0} years old.".format(age,name))

# f string
name = input()
age = input()
print(f"Hello, My name is {name} and I am {age} years old.")


# Finding data types
w = 525
f = 34.55
s = "Vishnu Akash"
b = True

print(type(w))
print(type(f))
print(type(s))
print(type(b))

# Extract some part of string
st_word = "Hello, Welcome to Bangalore! I am Vishnu Akash"
print(st_word[8:25])
