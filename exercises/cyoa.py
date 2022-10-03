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
                print("Speaking of which... what do you want to test first?")
            test_library()
            print("\nWhat do you wanna do now?")
            first_time = False
        elif user_choice == choice_two:
            if first_time:
                print("\nNow THIS should be interesting...")
            global points
            points += test_dorms(points)
            print(f"\nYou've earned ${points} in lawsuit money.")
            print("\nWhat do you wanna do now?")
            first_time = False
        elif user_choice == choice_three:
            exit_game()
            still_playing = False


def greet() -> None:
    print("\nWelcome to the University of North Carolina at Chapel Hill, the flagship of the")
    print(f"UNC school system, home to sunny skies, friendly people, and... lead water!? {CONFUSED_FACE}")
    global player 
    player = input("\nWhat's your name? ")


def test_library() -> None:
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
        i: int = randint(0, len(sink_results) - 1)
        sink_test(sink_results[i])
        
    
def fountain_test(result: float):
    print(f"\nResults loading {TEST_TUBE}...")
    factor: float = round((result / 15.0), 2)
    global points
    points += int(factor * 1000)
    if result == 193.0:
        print(f"\nSURPRISE! Upon retesting, lead levels jumped from 185.0 to {result} ppb, ~{factor} times the EPA minimum regulated amount!\nThat's a lot of lead!!!!")
    else:
        print(f"\nLead levels in this fountain are {result} ppb, which is ~{factor} times the EPA minimum regulated amount!")
    print(f"You have received ${points} in lawsuit money.")
    if points >= 1000:
        print("\nAt this rate, you're gonna be rolling in dough after four years of undergrad!")


def sink_test(result: float):
    print(f"\nResults loading {TEST_TUBE}...")
    factor: float = round((result / 15.0), 2)
    global points
    points += int(factor * 1000)
    print(f"\nLead levels in this sink are {result} ppb, which is ~{factor} times the EPA minimum regulated amount!")
    print(f"\nYou have received ${points} in lawsuit money.")
    if points >= 1000:
        print("\nAt this rate, you're gonna be rolling in dough after four years of undergrad!")


def test_dorms(x: int) -> int:
    dorm_names_years: tuple[str, int] = ["Alderman", 1937, "Alexander", 1939, "Avery", 1958, "Carmichael", 1986, "Cobb", 1952, "Conner", 1948, "Craige", 1962, "Craige North", 2002, "Ehringhaus", 1962, "Everett", 1928, "Graham", 1924, "Grimes", 1922, "Hardin", 2002, "Hinton James", 1967, "Horton", 2002, "Joyner", 1947, "Kenan", 1939, "Koury", 2002, "Lewis", 1924, "Magnum", 1922, "Manly", 1922, "McClinton", 1924, "McIver", 1939, "Morrison", 1965, "Old East", 1795, "Old West", 1823, "Parker", 1958, "Rams 1", 2006, "Rams 2", 2006, "Rams 3", 2006, "Rams 4", 2006, "Rams 5", 2006, "Stacy", 1938, "Spencer", 1924, "Teague", 1958, "Ruffin", 1922, "Winston", 1948]
    dorm_input: str = input("\nWhat dorm do you live in?\n> ")
    
    i: int = 0
    while i < len(dorm_names_years):
        if dorm_names_years[i] == dorm_input:
            print(f"\nThis dorm was built in {dorm_names_years[i + 1]}!")
            if dorm_names_years[i + 1] == 1795:
                print("WOW, The Big Kahuna! This is the oldest dorm on campus, meaning it has the highest lead levels of them all. Who needs a scholarship when you've got all this money!?")
                global points
                return 10000
            elif 1900 < dorm_names_years[i + 1] < 1930:
                print("That's one the oldest dorms on campus, so it's likely to have the most lead! Lucky you!")
                return randint(4001, 6000)
            elif 1931 < dorm_names_years[i + 1] < 1960:
                print("That dorm's pretty old, but not the oldest there is. You're only getting moderate amount of lead!")
                return randint(2001, 4000)
            elif 1961 < dorm_names_years[i + 1] < 1990:
                print(f"You're on South campus eh? That's gonna be slim pickings; you're probably below the EPA minimum {SHRUGGING_EMOJI}")
                return randint(0, 2000)
            elif dorm_names_years[i + 1] > 1991:
                print("Dang, you're living in one of the modern dorms. No lead (or money) for you; better luck next year!")
                return 0
        i += 2


def exit_game() -> None:
    print(f"\nYou're right {player}, so what if there's a little lead poisoning? Kids these days have it too easy anyway!")
    print(f"You earned ${points} in lawsuit money.")


if __name__ == "__main__":
    main()