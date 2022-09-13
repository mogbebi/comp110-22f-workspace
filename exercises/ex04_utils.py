"""EX04 – A 'list' utility function!"""

__author__ = "730480375"

def all(list_input: list, match: int) -> bool:
    i: int = 0
    all_match: bool = True
    while i < len(list_input) and all_match:
        if(list_input[i]) != match:
            all_match = False
        else:
            i += 1
    if all_match:
        return True
    else:
        return False


def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    max_value: int = input[0]
    while i < len(input) - 1:
        if input[i] < input[i + 1]:
            max_value = input[i + 1]
            i += 1
        else:
            i += 1

    return print(max_value)


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    i: int = 0
    all_match: bool  = True
    while all_match and i < len(list_1) or all_match and i < len(list_2):
        if list_1[i] != list_2[i]:
            all_match = False
        else:
            i += 1
    if all_match:
        return True
    else:
        return False