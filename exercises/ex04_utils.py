"""EX04 – List utility functions!"""

__author__ = "730480375"


def all(list_input: list[int], match: int) -> bool:
    """A function that checks that all the ints in a list match an single integer input."""
    i: int = 0
    all_match: bool = True
    if len(list_input) == 0:
        return False
    else:
        while i < len(list_input) and all_match:
            if list_input[i] != match or len(list_input) == 0:
                all_match = False
            else:
                i += 1
        if all_match:
            return True
        else:
            return False


def max(input: list[int]) -> int:
    """A function that determines the highest value from a list of ints."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    max_value: int = input[0]
    if len(input) == 1:
        return input[0]
    else:
        while i < len(input) - 1:
            if input[i] < input[i + 1] and input[i + 1] > max_value:
                max_value = input[i + 1]
                i += 1
            else:
                i += 1
        return max_value


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """A function that determines if two lists have deep equality."""
    if len(list_1) == 0 and len(list_2) == 0:
        return True
    if len(list_1) != len(list_2):
        return False
    else:
        i: int = 0
        all_match: bool = True
        while all_match and i < len(list_1):
            if list_1[i] != list_2[i]:
                all_match = False
            else:
                i += 1
        if all_match:
            return True
        else:
            return False