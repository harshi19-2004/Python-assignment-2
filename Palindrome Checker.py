# Q17 - Palindrome Checker

user_input = input("Enter word/number: ")

# convert to lowercase for case-insensitive comparison
cleaned = user_input.lower()
reversed_str = cleaned[::-1]  # reverse the string

print(f"Original : {user_input}")
print(f"Reversed : {user_input[::-1]}")

# compare original and reversed to check palindrome
if cleaned == reversed_str:
    print("Result   : PALINDROME")
else:
    print("Result   : NOT a palindrome")