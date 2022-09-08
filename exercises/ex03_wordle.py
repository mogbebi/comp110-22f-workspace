"""EX03 - Structured Wordle (now with functions)!"""

__author__ = "730480375"


def contains_char(word_searched: str, current_letter: str) -> bool:
    """Determines whether an input letter is present in an input word."""
    assert len(current_letter) == 1
    i: int = 0
    done_scanning: bool = False
    while i < len(word_searched) and not done_scanning:
        if word_searched[i] == current_letter:
            done_scanning = True
        else:
            i += 1
    if done_scanning:
        return True
    else:
        return False


def emojified(guess: str, secret_word: str) -> str:
    """Compares the secret word with the guess of the same length and outputs the emojified version of the guess."""
    assert len(guess) == len(secret_word)
    i: int = 0
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    square_output: str = ""
    while i < len(secret_word):
        if guess[i] == secret_word[i]:
            square_output = square_output + GREEN_BOX
            i += 1
        elif contains_char(secret_word, guess[i]):
            square_output = square_output + YELLOW_BOX
            i += 1
        else:
            square_output = square_output + WHITE_BOX
            i += 1
    return square_output


def input_guess(word_length: int) -> str:
    """Assures that the length of a guess is the same as the input word length number."""
    new_guess: str = input(f"Enter a {word_length} character word: ")
    
    while word_length != len(new_guess):
        new_guess = input(f"That wasn't {word_length} chars! Try again: ")
    return new_guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn_number: int = 0
    secret_word: str = "codes"
    still_playing: bool = True
    while turn_number < 6 and still_playing:
        """Prints the current turn number."""
        print(f"=== Turn {turn_number + 1}/6 ===")
        """Sets a variable equal to the output of the input_guess function."""
        new_guess: str = input_guess(len(secret_word))
        """Uses the new_guess variable in the emojified function to turn the guess into the emojified output."""
        print(emojified(new_guess, secret_word))
        """Determines if the guess matches the secret word and acts accordingly."""
        if new_guess == secret_word:
            """If the guess and word matches, the victory message is displayed and the game ends."""
            print(f"You won in {turn_number + 1}/6 turns!")
            still_playing = False
        else:
            """If the guess is incorrect, the loop continues."""
            turn_number += 1

    """If the loop ends and the player has used up all 6 guesses, the game over message is displayed."""
    if turn_number == 6:
        print("X/6 – Sorry, try again tomorrow!")


"""Allows this function to be available as a Python module."""
if __name__ == "__main__":
    main()