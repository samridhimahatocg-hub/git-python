
full_name = input("Enter your full name: ")

cleaned_name = full_name.strip()

print("Original Input:", full_name)
print("Cleaned Name:", cleaned_name)
print("Uppercase:", cleaned_name.upper())
print("Lowercase:", cleaned_name.lower())
print("Title Case:", cleaned_name.title())
print("Length:", len(cleaned_name))
print("First Character:", cleaned_name[0])
print("Last Character:", cleaned_name[-1])

char = input("Enter a character to check: ")
print(f"Does the name contain '{char}'?", char in cleaned_name)

sentence = input("Enter a sentence: ")

print("Original Sentence:", sentence)
print("Number of Characters:", len(sentence))
print("Number of Words:", len(sentence.split()))
print("First Character:", sentence[0])
print("Last Character:", sentence[-1])
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("Title Case:", sentence.title())
print("Contains 'Python'?", "Python" in sentence)

char = input("Enter a character to count: ")
print(f"'{char}' occurs {sentence.count(char)} times")


first_name = input("Enter first name: ").strip()
last_name = input("Enter last name: ").strip()
city = input("Enter city: ").strip()
course = input("Enter course: ").strip()
age = int(input("Enter age: "))

full_name = first_name + " " + last_name

print("Full Name (Title Case):", full_name.title())
print("Full Name (Uppercase):", full_name.upper())
print("Full Name (Lowercase):", full_name.lower())
print("Length of Full Name:", len(full_name))
print("First Character:", full_name[0])
print("Last Character:", full_name[-1])
print("City:", city)
print("Course:", course)
print(f"Age: {age}")

print("Contains 'Python'?", "Python" in course)

new_course = course.replace("Python", "AI")
print("Updated Course:", new_course)
print("Number of Words in Course:", len(course.split()))



