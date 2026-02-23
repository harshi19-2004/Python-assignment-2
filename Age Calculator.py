# Age Calculator Program
# This program calculates age details based on birth year

from datetime import datetime   # importing to get current year

try:
    # taking birth year input from user
    birth_year = int(input("Enter your birth year : "))

    # getting current year
    current_year = datetime.now().year

    # checking for invalid year
    if birth_year > current_year or birth_year <= 0:
        print("Please enter a valid birth year.")
    else:
        # calculating current age
        current_age = current_year - birth_year
        print("Current Age:", current_age, "years")

        # calculating age in months
        age_in_months = current_age * 12
        print("Age in Months:", age_in_months)

        # calculating age in days (approx 365 days per year)
        age_in_days = current_age * 365
        print("Age in Days (approx):", age_in_days)

        # calculating age in hours
        age_in_hours = age_in_days * 24
        print("Age in Hours:", age_in_hours)

        # calculating age in minutes
        age_in_minutes = age_in_hours * 60
        print("Age in Minutes:", age_in_minutes)

        # years remaining to reach 100
        years_to_100 = 100 - current_age
        print("Years until age 100:", years_to_100)

except ValueError:
    print("Invalid input! Please enter birth year in numbers only.")