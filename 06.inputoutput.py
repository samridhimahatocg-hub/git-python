name=input("Enter your name: ")
city = input("Enter your city: ")
print("Your city is", city)

name = input("Enter your name: ")
age = input("Enter your age: ")
print("Name:", name)
print("Age:", age)

value = input("Enter something: ")
print("Type:", type(value))

# 6 
first = input("Enter first name: ")
last = input("Enter last name: ")
print(first, last)

# 7 
name = input("Enter name: ")
city = input("Enter city: ")
college = input("Enter college: ")
print(name, city, college)

# 8
a, b = input("Enter two names: ").split()
print(a, b)


# 10
x, y, z = input("Enter three words: ").split()
print(x)
print(y)
print(z)

num = int("25")

num = float("25.5")

# 13
s = str(100)

# 14
n = int(input("Enter an integer: "))
print(type(n))

# 15.
f = float(input("Enter a float: "))
print(type(f))



# 17.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a + b)

# 18
name = "Rahul"
age = 20
print(f"My name is {name} and I am {age} years old.")

# 19
a, b = 10, 20
print(f"Sum = {a + b}")

# 20
name = input("Enter name: ")
age = int(input("Enter age: "))
print(f"My name is {name} and I am {age} years old.")

# 21
price = float(input("Enter price: "))
print(f"Price: {price:.2f}")


# 23
product = input("Enter product name: ")
price = float(input("Enter price: "))
qty = int(input("Enter quantity: "))
print(f"Product: {product}, Price: {price}, Quantity: {qty}")

# 24
print("A", "B", "C")   

# 25
print("2026", "08", "19", sep="-")

# 26
print("Hello", end=" ")
print("World")

# 27
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(f"First number: {a}")
print(f"Second number: {b}")
print(f"Sum: {a + b}")

# 28
price = float(input("Enter price: "))
qty = int(input("Enter quantity: "))
total = price * qty
print(f"Price: {price}, Quantity: {qty}, Total: {total}")

# 29
name = input("Enter name: ")
age = int(input("Enter age: "))
marks = float(input("Enter marks: "))
print(f"Student: {name}, Age: {age}, Marks: {marks}")

# 30
name = input("Enter name: ")
age = int(input("Enter age: "))
height = float(input("Enter height: "))
city = input("Enter city: ")
print(f"Name: {name}, Age: {age}, Height: {height:.2f}, City: {city}")