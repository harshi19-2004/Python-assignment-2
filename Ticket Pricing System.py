# Q9 - Ticket Pricing System

try:
    age = int(input("Enter age: "))
    day = input("Enter day of the week: ").strip().lower()
    tickets = int(input("Enter number of tickets: "))

    # set base price based on age
    if age < 0:
        print("Age cannot be negative.")
    elif age < 3:
        base_price = 0
        category = "Free (Under 3)"
    elif age <= 12:
        base_price = 150
        category = "Child"
    elif age <= 59:
        base_price = 300
        category = "Adult"
    else:
        base_price = 200
        category = "Senior"

    # 20% discount on weekends
    weekend = ["friday", "saturday", "sunday"]
    if day in weekend:
        discount = base_price * 0.20
    else:
        discount = 0

    price_per_ticket = base_price - discount
    total = price_per_ticket * tickets

    print(f"\nCategory       : {category}")
    print(f"Base Price     : Rs.{base_price}")
    print(f"Discount       : Rs.{discount}")
    print(f"Price/Ticket   : Rs.{price_per_ticket}")
    print(f"Total Amount   : Rs.{total}")

except ValueError:
    print("Invalid input! Please enter correct values.")