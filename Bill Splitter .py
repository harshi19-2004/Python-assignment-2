# Q5 - Bill Splitter Program
# This program calculates restaurant bill details and splits the amount per person.

try:
    # Taking user inputs
    total_bill = float(input("Enter total bill: "))
    number_of_people = int(input("Number of people: "))
    tax_percentage = float(input("Tax percentage: "))
    tip_percentage = float(input("Tip percentage: "))

    # Checking for invalid values
    if total_bill < 0 or number_of_people <= 0 or tax_percentage < 0 or tip_percentage < 0:
        print("Invalid input! Values cannot be negative and people must be more than 0.")
    else:
        # Subtotal (same as total bill before tax)
        subtotal = total_bill

        # Calculating tax amount
        tax_amount = (subtotal * tax_percentage) / 100

        # Amount after adding tax
        bill_after_tax = subtotal + tax_amount

        # Calculating tip on amount after tax
        tip_amount = (bill_after_tax * tip_percentage) / 100

        # Final total bill
        final_total = bill_after_tax + tip_amount

        # Amount per person
        amount_per_person = final_total / number_of_people

        # Displaying output
        print("\n=== BILL BREAKDOWN ===")
        print(f"Subtotal: ₹{subtotal:.2f}")
        print(f"Tax ({tax_percentage}%): ₹{tax_amount:.2f}")
        print(f"After tax: ₹{bill_after_tax:.2f}")
        print(f"Tip ({tip_percentage}%): ₹{tip_amount:.2f}")
        print(f"Total: ₹{final_total:.2f}")
        print(f"Per person: ₹{amount_per_person:.2f}")

except ValueError:
    print("Invalid input! Please enter numeric values only.")
except Exception as e:
    print("Something went wrong:", e)