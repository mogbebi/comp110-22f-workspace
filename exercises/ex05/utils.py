"""Skeleton functions and implementations for EX05."""

__author__ = "730480375"


def only_evens(input: list[int]) -> list[int]:
    """Returns all the even ints in a given list of ints."""
    i: int = 0
    list_output: list[int] = list()
    if len(input) == 0:
        return list_output
    else:
        while i < len(input):
            if input[i] % 2 == 0:
                list_output.append(input[i])
                i += 1
            else:
                i += 1
        return list_output


def concat(list_1: list[int], list_2: list[int]) -> list[int]:
    """Concatenates two list of ints into one larger list of ints in the order specified."""
    if len(list_1) == 0:
        return list_2
    else:
        list_output: list[int] = list()
        i: int = 0
        while i < len(list_1):
            list_output.append(list_1[i])
            i += 1
        i = 0
        while i < len(list_2):
            list_output.append(list_2[i])
            i += 1
        return list_output


def sub(input: list[int], start: int, end: int) -> list[int]:
    """Returns the sub-list of a given a list of ints, a start index, and end index (non-inclusinve)."""
    list_output: list[int] = list()
    if len(input) == 0:
        return list_output
    else:
        i = start
        while i < end:
            list_output.append(input[i])
            i += 1
        return list_output