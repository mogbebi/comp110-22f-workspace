"""A choose-your-own-adventure game about some refreshing, non-toxic water!"""

__author__ = "730480375"

from random import randint

# Magic numbers
CONFUSED_FACE: str = "\U0001F928"
LIBRARY_EMOJI: str = "\U0001F3EB"
DORM_EMOJI: str = "\U0001F3D8"
QUIET_EMOJI: str = "\U0001F92B"
FOUNTAIN_EMOJI: str = "\U000026F2"
SINK_EMOJI: str = "\U0001F6B0"
TEST_TUBE: str = "\U0001F9EA"
WINKING_EMOJI: str = "\U0001F609"
SHRUGGING_EMOJI: str = "\U0001F937"

# Global variables
player: str = ""
points: int = 0


def main() -> None:
    """Main function to enter game loop."""
    choice_one: str = "Test water in Wilson Library"
    choice_two: str = "Test water in dorms"
    choice_three: str = "Ignore the issue"
    option_tree: str = f"1. {choice_one} {LIBRARY_EMOJI}\n2. {choice_two} {DORM_EMOJI}\n3. {choice_three} {QUIET_EMOJI}\n> "
    still_playing: bool = True
    first_time: bool = True
    greet()
    print(f"\nWell {player}, seems we have a teeeeeennny-weeny little crisis on our hands...")
    print("\nWhat do you wanna do?")
    while still_playing:
        user_choice: str = input(option_tree)
        while user_choice != choice_one and user_choice != choice_two and user_choice != choice_three:
            user_choice = input(f"\nThat's not an option! Please type one of the options listed below:\n{option_tree}")
        if user_choice == choice_one:
            if first_time:
                print(f"\nSeems like a good place to start! Let's put our facilites to the test eh {WINKING_EMOJI}?")
            test_library()
            print("\nWhat do you wanna do now?")
            first_time = False
        elif user_choice == choice_two:
            if first_time:
                print("\nNow THIS should be interesting...")
            global points
            points += test_dorms(points)
            print(f"\nYou've earned ${points} in lawsuit money.")
            if points >= 1000:
                print("\nAt this rate, you're gonna be rolling in dough after four years of undergrad!")
            print("\nWhat do you wanna do now?")
            first_time = False
        elif user_choice == choice_three:
            exit_game()
            still_playing = False


def greet() -> None:
    """Welcomes the player, gives context to the game, and assigns the player variable to the player's name input."""
    print("\nWelcome to the University of North Carolina at Chapel Hill, the flagship of the")
    print(f"UNC school system, home to sunny skies, friendly people, and... lead water!? {CONFUSED_FACE}")
    global player 
    player = input("\nWhat's your name? ")


def test_library() -> None:
    """Function that gives calculated "lawsuit money" based on real EHS test results chosen from a list, and update the points value accordingly."""
    fountain_results: list[float] = [9.0, 3.1, 185.0, 2.0]
    sink_results: list[float] = [2.9, 4.6, 3.1, 3.6, 12.1, 2.0, 4.0, 7.0, 96.3, 24.4, 6.3, 30.3, 2.6, 2.8]
    test_fountain: str = "Test fountain"
    test_sink: str = "Test sink"
    option_tree: str = f"{test_fountain} {FOUNTAIN_EMOJI}\n{test_sink} {SINK_EMOJI}\n> "
    print("\nWhich one do you want to test?")
    test_choice: str = input(option_tree)
    while test_choice != test_fountain and test_choice != test_sink:
        test_choice = input(f"\nThat's not an option! Please type one of the options listed below:\n{option_tree}")
    if test_choice == test_fountain:
        i: int = randint(0, len(fountain_results) - 1)
        if i == 2:
            fountain_test(193.0)
        else:
            fountain_test(fountain_results[i])
    else:
        i = randint(0, len(sink_results) - 1)
        sink_test(sink_results[i])
        
    
def fountain_test(result: float) -> None:
    """Smaller function that calculates the "lawsuit money" earned based on the randomly chosen EHS lead result from a fountain."""
    print(f"\nResults loading {TEST_TUBE}...")
    factor: float = round((result / 15.0), 2)
    global points
    points += int(factor * 1000)
    if result == 193.0:
        print(f"\nSURPRISE! Upon retesting, lead levels jumped from 185.0 to {result} ppb, ~{factor} times the EPA minimum regulated amount!\nThat's a lot of lead!!!!")
    else:
        print(f"\nLead levels in this fountain are {result} ppb, which is ~{factor} times the EPA minimum regulated amount!")
    print(f"\nYou have received ${points} in lawsuit money.")
    if points >= 1000:
        print("\nAt this rate, you're gonna be rolling in dough after four years of undergrad!")


def sink_test(result: float) -> None:
    """Smaller function that calculates the "lawsuit money" earned based on the randomly chosen EHS lead result from a sink."""
    print(f"\nResults loading {TEST_TUBE}...")
    factor: float = round((result / 15.0), 2)
    global points
    points += int(factor * 1000)
    print(f"\nLead levels in this sink are {result} ppb, which is ~{factor} times the EPA minimum regulated amount!")
    print(f"\nYou have received ${points} in lawsuit money.")
    if points >= 1000:
        print("\nAt this rate, you're gonna be rolling in dough after four years of undergrad!")


def test_dorms(x: int) -> int:
    """Function that calculates the "lawsuit money" based on how old the user-inputted dorm is, and updates the player value accordingly."""
    dorm_names: list[str] = ["Alderman", "Alexander", "Avery", "Carmichael", "Cobb", "Conner", "Craige", "Craige North", "Ehringhaus", "Everett", "Graham", "Grimes", "Hardin", "Hinton James", "Horton", "Joyner", "Kenan", "Koury", "Lewis", "Magnum", "Manly", "McClinton", "McIver", "Morrison", "Old East", "Old West", "Parker", "Rams 1", "Rams 2", "Rams 3", "Rams 4", "Rams 5", "Stacy", "Spencer", "Teague", "Ruffin", "Winston"]
    dorm_years: list[int] = [1937, 1939, 1958, 1986, 1952, 1948, 1962, 2002, 1962, 1928, 1924, 1922, 2002, 1967, 2002, 1947, 1939, 2002, 1924, 1922, 1922, 1924, 1939, 1965, 1795, 1823, 1958, 2006, 2006, 2006, 2006, 2006, 1938, 1924, 1958, 1922, 1948]
    dorm_input: str = input("\nWhat dorm are you testing?\n> ")
    i: int = 0
    while i < len(dorm_names):
        if dorm_names[i] == dorm_input:
            print(f"\nThis dorm was built in {dorm_years[i]}!")
            if dorm_years[i] == 1795:
                print("WOW, The Big Kahuna! This is the oldest dorm on campus, meaning it has the highest lead levels of them all.\nWho needs a scholarship when you've got all this money!?")
                global points
                test_dorm_output: int = 10000
                i += 1
            elif 1900 < dorm_years[i] < 1930:
                print("That's one the oldest dorms on campus, so it's likely to have the most lead! Lucky you!")
                test_dorm_output = randint(667, 1000)
                i += 1
            elif 1931 < dorm_years[i] < 1960:
                print("That dorm's pretty old, but not the oldest there is. You're only getting moderate amount of lead!")
                test_dorm_output = randint(334, 666)
                i += 1
            elif 1961 < dorm_years[i] < 1980:
                print(f"You're on South campus eh? That's gonna be slim pickings; you're probably below the EPA minimum {SHRUGGING_EMOJI}")
                test_dorm_output = randint(1, 333)
                i += 1
            elif dorm_years[i] > 1981:
                print("Dang, you're living in one of the modern dorms. No lead (or money) for you; better luck next year!")
                test_dorm_output = 0
                i += 1
        else:
            i += 1
    return test_dorm_output


def exit_game() -> None:
    """Function to end the game when the player chooses the ignore the issue."""
    print(f"\nYou're right {player}, so what if there's a little lead poisoning? Kids these days have it too easy anyway!")
    print(f"\nYou earned ${points} in lawsuit money.\n")


if __name__ == "__main__":
    main()