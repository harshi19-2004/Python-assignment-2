# String Manipulator Program
# This program performs different operations on a sentence entered by the user

try:
    # Taking input from user
    user_sentence = input("Enter a sentence: ")

    # Checking if input is empty
    if user_sentence.strip() == "":
        print("You entered an empty sentence. Please run the program again.")
    else:
        # 1. Original sentence
        print("Original:", user_sentence)

        # 2. Total characters (with spaces)
        total_char_with_spaces = len(user_sentence)
        print("Characters (with spaces):", total_char_with_spaces)

        # 3. Total characters (without spaces)
        sentence_without_spaces = user_sentence.replace(" ", "")
        total_char_without_spaces = len(sentence_without_spaces)
        print("Characters (without spaces):", total_char_without_spaces)

        # 4. Total words
        word_list = user_sentence.split()
        total_words = len(word_list)
        print("Words:", total_words)

        # 5. Uppercase
        print("UPPERCASE:", user_sentence.upper())

        # 6. Lowercase
        print("lowercase:", user_sentence.lower())

        # 7. Title Case
        print("Title Case:", user_sentence.title())

        # 8. First word
        print("First word:", word_list[0])

        # 9. Last word
        print("Last word:", word_list[-1])

        # 10. Reversed sentence
        reversed_sentence = user_sentence[::-1]
        print("Reversed:", reversed_sentence)

except Exception as e:
    print("Something went wrong:", e)