"""Practice with dictionary functions."""

__author__ = "730480375"


def invert(dict_input: dict[str, str]) -> dict[str, str]:
    """Inverts a dict input by reversing each key-pair value."""
    inverted_dict: dict[str, str] = dict()
    enumerated_list: list[str] = list()
    if len(dict_input) == 0:
        return inverted_dict
    for key in dict_input:
        enumerated_list.append(dict_input[key])
    i: int = 0
    while i < len(enumerated_list) - 1:
        j: int = i + 1
        while j < len(enumerated_list):
            if enumerated_list[i] == enumerated_list[j]:
                raise KeyError("That's an invalid input! Make sure none of your values are the same.")
            else:
                j += 1
        i += 1
    for key in dict_input:
            inverted_dict[dict_input[key]] = key
    return inverted_dict


def favorite_color(names_colors: dict[str, str]) -> str:
    """Outputs a favorite color based on which value (color) occurs most frequently."""
    enumerated_list: list[str] = list()
    if len(names_colors) == 0:
        return "No winner!"
    for key in names_colors:
        enumerated_list.append(names_colors[key])
    i: int = 0
    first_winning_color: bool = True
    winning_color: str = enumerated_list[0]
    while i < len(enumerated_list) - 1:
        j: int = i + 1
        while j < len(enumerated_list):
            if enumerated_list[i] == enumerated_list[j] and first_winning_color:
                winning_color = enumerated_list[i]
                first_winning_color = False
                j += 1
            else:
                j += 1
        i += 1
    return winning_color


def count(list_input: list[str]) -> dict[str, int]:
    """Outputs a dictionary that counts the number of times a string appears in the list."""
    dict_output: dict[str, int] = dict()
    if len(list_input) == 0:
        return dict_output
    for item in list_input:
        if item in dict_output:
            dict_output[item] += 1
        else:
            dict_output[item] = 1
    return dict_output