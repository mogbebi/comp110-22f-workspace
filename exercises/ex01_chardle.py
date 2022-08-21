"""EX01 – Chardle – A cute step toward Wordle."""

__author__ = "730480375"

word_input: str = input("Enter a 5-character word: ")

if len(word_input) != 5:
    print("Error: Word must contain 5 characters")
    exit()

letter_input: str = input("Enter a single character: ")

if len(letter_input) != 1:
    print("Error: Character must be a single character.")
    exit()

matching_letters: int = 0

print("Searching for " + letter_input + " in " + word_input)

if letter_input == word_input[0]:
    print(letter_input + " found at index 0")
    matching_letters = matching_letters + 1

if letter_input == word_input[1]:
    print(letter_input + " found at index 1")
    matching_letters = matching_letters + 1

if letter_input == word_input[2]:
    print(letter_input + " found at index 2")
    matching_letters = matching_letters + 1

if letter_input == word_input[3]:
    print(letter_input + " found at index 3")
    matching_letters = matching_letters + 1

if letter_input == word_input[4]:
    print(letter_input + " found at index 4")
    matching_letters = matching_letters + 1

if matching_letters == 0:
    print("No instances of " + letter_input + " found in " + word_input)

if matching_letters == 1:
    print(str(matching_letters) + " instance of " + letter_input + " found in " + word_input)

if matching_letters > 1:
    print(str(matching_letters) + " instances of " + letter_input + " found in " + word_input)

