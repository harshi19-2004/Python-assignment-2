# Q19 - Text Analysis Functions

def count_words(text):
    # split by spaces and count the words
    words = text.split()
    return len(words)

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

def count_consonants(text):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    count = 0
    for char in text:
        if char in consonants:
            count += 1
    return count

def reverse_text(text):
    return text[::-1]

def is_palindrome(text):
    # remove spaces and convert to lowercase for checking
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

def remove_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""
    for char in text:
        if char not in vowels:
            result += char
    return result

def word_frequency(text):
    words = text.lower().split()
    frequency = {}
    for word in words:
        # remove punctuation from word edges
        word = word.strip(".,!?")
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

def longest_word(text):
    words = text.split()
    if not words:
        return ""
    # find the word with maximum length
    long_word = max(words, key=len)
    return long_word

def analyze_text(text):
    # call all functions and display results
    print("\n=== TEXT ANALYSIS ===")
    print(f"Words       : {count_words(text)}")
    print(f"Vowels      : {count_vowels(text)}")
    print(f"Consonants  : {count_consonants(text)}")
    print(f"Reversed    : {reverse_text(text)}")
    print(f"Palindrome  : {'Yes' if is_palindrome(text) else 'No'}")
    print(f"Without vowels: {remove_vowels(text)}")

    lw = longest_word(text)
    print(f"Longest word: {lw} ({len(lw)} letters)")

    freq = word_frequency(text)
    freq_str = ", ".join(f"{w}: {c}" for w, c in freq.items())
    print(f"Word Frequency: {freq_str}")


# main program
try:
    user_text = input("Enter text: ")

    if user_text.strip() == "":
        print("You did not enter any text.")
    else:
        analyze_text(user_text)

except Exception as e:
    print(f"Something went wrong: {e}")