#1.
# number=int(input("Enter a number: "))
# if number>10:
#     print("the number is greater than 10")

# #2.
# age=int(input("Enter your age: "))
# if age>=18:
#     print("adult")

# #3.
# number=int(input("Enter a number: "))
# if number>0:
#     print("the number is positive")

# #4.
# marks=int(input("Enter marks: "))
# if marks>=40:
#     print("pass")

# #5.
# number=int(input("Enter a number: "))
# if number==0:    
#     print("zero")

# #if-else statements


# #6.
# number=int(input("Enter a number: "))
# if number>=0:
#     print("positive")
# else:
#     print("negative")

# #7.
# age=int(input("Enter your age: "))
# if age>=18:
#     print("adult")
# else:
#     print("minor")    

# #8.
# number=int(input("Enter the number: "))
# if number % 2==0:
#     print("even")
# else:
#     print("odd")

# #9.
# marks=int(input("Enter marks"))
# if marks>=40:
#     print("pass")
# else:
#     print("fail")        

#10
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# if num1 > num2:
#     print(num1, "is greater")
# else:
#     print(num2, "is greater")

#11.
# marks=int(input("Enter your marks:"))
# if marks>=90:
#     print("A")

# elif 75<=marks<89 :    
#     print("B")

# elif 60<=marks<74 :
#     print("C")

# elif 40<marks<59 :
#     print("D")

# else :
#     print("F")

#12.

# number=int(input("Enter number : "))
# if number>0 :
#     print("the number is positive.")

# elif number<0 :
#     print("the number is negative.")

# elif number==0 :
#     print("the number is zero.")    

#13.

# day = int(input("Enter a number (1-7): "))

# if day == 1:
#     print("Monday")
# elif day == 2:
#     print("Tuesday")
# elif day == 3:
#     print("Wednesday")
# elif day == 4:
#     print("Thursday")
# elif day == 5:
#     print("Friday")
# else:
#     print("Other")





# #14.

# marks=int(input("enter your marks: "))

# if marks< 0 or marks> 100:
#     print("Invalid input")

# elif marks>=90 and marks<=100 :
#     print("Excellent")

# elif marks<=90 and marks>=70:
#     print("Good")    

# elif marks<70 and marks>=40 :    
#     print("Pass")

# else:
#     print("Fail")    


# #15.

# num = int(input("Enter a number: "))

# if num == 1:
#     print("1")
# elif num == 2:
#     print("2")
# elif num == 3:
#     print("3")
# else:
#     print("Other")
    

#17.

marks=int(input("Enter marks: "))

if marks>=40:
    if marks>=75 :
        print("good")
    else:
        print("passed")

else:
    print("failed")            


#16.
age = int(input("Enter your age: "))

if age >= 18:
    if age <= 60:
        print("Between 18 and 60")


num = int(input("Enter a number: "))

if num > 0:
    if num > 100:
        print("Positive and greater than 100")
    else:
        print("Positive but not greater than 100")
else:
    print("Not positive")


#19. 
age = int(input("Enter age: "))

if age >= 18:
    if age >= 60:
        print("Senior Citizen")
    else:
        print("Adult")
else:
    print("Minor")
20. 
num = int(input("Enter a number: "))

if num != 0:
    if num > 0:
        print("Positive")
    else:
        print("Negative")
else:
    print("Zero")


#21.
age = int(input("Enter age: "))
marks = int(input("Enter marks: "))

if age >= 18 and marks >= 40:
    print("Eligible")
else:
    print("Not eligible")


22. 
num = int(input("Enter a number: "))

if num < 10 or num > 100:
    print("Special")
else:
    print("Not special")


23. 
age = int(input("Enter age: "))
has_id = True  # or False

if age >= 18 and has_id:
    print("Allowed")
else:
    print("Not allowed")


24. 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > 10 and b > 10:
    print("Both are greater than 10")
else:
    print("Condition not satisfied")


25. 
num = int(input("Enter a number: "))

if num < 0 or num > 100:
    print("Condition satisfied")
else:
    print("Condition not satisfied")


 #26.
is_closed = False

if not is_closed:
    print("Open")
else:
    print("Closed")


27. 
num = int(input("Enter a number: "))

if num >= 10 and num <= 50:
    print("Number is between 10 and 50")
else:
    print("Not in range")


28. 
num = int(input("Enter a number: "))

if num < 10 or num > 50:
    print("Outside range")
else:
    print("Within range")


29. 
is_student = True
has_id = True
has_ticket = True

if is_student and has_id and has_ticket:
    print("Allowed")
else:
    print("Not allowed")


30. 
age = int(input("Enter age: "))
marks = int(input("Enter marks: "))
has_id = True  # or False

if age >= 18 and marks >= 40 and has_id:
    print("Eligible")
else:
    print("Not eligible")


