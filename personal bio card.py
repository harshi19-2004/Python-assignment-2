# Personal Bio Card Program
# This program takes user details and displays them in a formatted box

# Taking input from user
full_name = input("Enter your full name: ")

# Using try-except to handle invalid age input
try:
    age = int(input("Enter your age: "))
    
    # Checking for negative or zero age
    if age <= 0:
        print("Age must be a positive number.")
        exit()

except ValueError:
    print("Invalid input! Please enter age in numbers only.")
    exit()

course_name = input("Enter your course: ")
college_name = input("Enter your college name: ")
email_address = input("Enter your email: ")

# Displaying formatted bio card
print("\n" + "=" * 45)
print("              STUDENT BIO CARD")
print("=" * 45)

print("Name    :", full_name)
print("Age     :", age, "years")
print("Course  :", course_name)
print("College :", college_name)
print("Email   :", email_address)

print("=" * 45)