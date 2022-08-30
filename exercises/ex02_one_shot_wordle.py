"""EX02 One-Shot Wordle – another step towards Wordle"""

__author__ = "730480375"

secret: str = "python"
letter_number: int = len(secret)
guess: str = input(f"What is your {letter_number}-letter guess? ")
i: int = 0
square_output: str = ""
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while len(guess) != letter_number:
    guess = input(f"That was not {letter_number} letters! Try again: ")

while i < letter_number:
    if guess[i] == secret[i]:
        square_output = square_output + GREEN_BOX
        i = i + 1
    else:
        j: int = 0
        while j < letter_number:
            if secret[j] == guess[i]:
                square_output = square_output + YELLOW_BOX
                j = letter_number + 1
            else:
                j = j + 1
        if j == letter_number:
            square_output = square_output + WHITE_BOX
            i = i + 1
        else:
            i = i + 1

print(square_output)

if guess != secret:
    print("Not quite. Play again soon!")
else:
    print("Woo! You got it!")