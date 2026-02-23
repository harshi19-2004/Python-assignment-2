# Q6 - Grade Calculator
# This program calculates total marks, percentage, grade and pass/fail result.

try:
    print("Enter marks for 5 subjects (out of 100 each):")

    # Taking inputs
    subject1 = float(input("Subject 1: "))
    subject2 = float(input("Subject 2: "))
    subject3 = float(input("Subject 3: "))
    subject4 = float(input("Subject 4: "))
    subject5 = float(input("Subject 5: "))

    # Storing marks in a list for easy processing
    marks_list = [subject1, subject2, subject3, subject4, subject5]

    # Checking if marks are within valid range
    for mark in marks_list:
        if mark < 0 or mark > 100:
            print("Invalid input! Marks should be between 0 and 100.")
            exit()

    # Calculating total and percentage
    total_marks = sum(marks_list)
    percentage = (total_marks / 500) * 100

    # Determining grade based on percentage
    if percentage >= 90:
        grade = "A+ (Outstanding)"
    elif percentage >= 80:
        grade = "A (Excellent)"
    elif percentage >= 70:
        grade = "B (Good)"
    elif percentage >= 60:
        grade = "C (Average)"
    elif percentage >= 50:
        grade = "D (Pass)"
    else:
        grade = "F (Fail)"

    # Checking pass or fail (all subjects must be >= 40)
    if all(mark >= 40 for mark in marks_list):
        result = "Pass"
    else:
        result = "Fail"

    # Displaying results
    print("\n=== RESULT ===")
    print(f"Marks: {marks_list}")
    print(f"Total Marks: {total_marks} / 500")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")
    print(f"Result: {result}")

except ValueError:
    print("Invalid input! Please enter numeric values only.")
except Exception as e:
    print("Something went wrong:", e)