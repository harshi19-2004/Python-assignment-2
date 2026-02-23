# Q7 - Temperature Converter
# This program converts temperatures between Celsius, Fahrenheit and Kelvin
# using a menu-based system.

def display_menu():
    print("\n===== Temperature Converter =====")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")


while True:
    display_menu()

    try:
        choice = int(input("Enter your choice (1-7): "))

        # Exit option
        if choice == 7:
            print("Exiting program... Thank you!")
            break

        # Checking valid range
        if choice < 1 or choice > 7:
            print("Invalid choice! Please select between 1 and 7.")
            continue

        # Taking temperature input
        temperature = float(input("Enter temperature value: "))

        # Conversion calculations
        if choice == 1:
            result = (temperature * 9/5) + 32
            print(f"{temperature}°C = {result:.2f}°F")

        elif choice == 2:
            result = (temperature - 32) * 5/9
            print(f"{temperature}°F = {result:.2f}°C")

        elif choice == 3:
            result = temperature + 273.15
            print(f"{temperature}°C = {result:.2f} K")

        elif choice == 4:
            result = temperature - 273.15
            print(f"{temperature} K = {result:.2f}°C")

        elif choice == 5:
            result = (temperature - 32) * 5/9 + 273.15
            print(f"{temperature}°F = {result:.2f} K")

        elif choice == 6:
            result = (temperature - 273.15) * 9/5 + 32
            print(f"{temperature} K = {result:.2f}°F")

    except ValueError:
        print("Invalid input! Please enter numeric values only.")
    except Exception as e:
        print("Something went wrong:", e)