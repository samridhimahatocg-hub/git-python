student_name = "Rahul"       # string
student_age = 20             # integer
student_height = 5.8         # float
is_student = True            # boolean
student_result = None        # NoneType

print(type(student_name))    # <class 'str'>
print(type(student_age))     # <class 'int'>
print(type(student_height))  # <class 'float'>
print(type(is_student))      # <class 'bool'>
print(type(student_result))  # <class 'NoneType'>

a = 50
b = 50.0
c = "50"

print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'str'>

a = True
b = "True"

print(type(a))  # <class 'bool'>
print(type(b))  # <class 'str'>


a = None
b = "None"

print(type(a))  # <class 'NoneType'>
print(type(b))  # <class 'str'>


value = 10
print("Before:", value, type(value))

value = "Ten"
print("After:", value, type(value))


product_name = "Laptop"
product_quantity = 5
product_price = 59999.99
product_available = True
product_discount = None

print(type(product_name))      
print(type(product_quantity))  
print(type(product_price))    
print(type(product_available)) 
print(type(product_discount)) 

print(10, type(10))        
print(10.0, type(10.0))    
print("10", type("10"))    
print(True, type(True))    
print("True", type("True")) 
print(None, type(None))     
print("None", type("None")) 