"""Unit tests for EX07 functions."""

from dictionary import invert, favorite_color, count

def test_invert_empty_dict() -> None:
    """Tests the edge case of an empty dictionary input."""
    empty_dictionary = {}
    assert invert(empty_dictionary) == {}


def test_invert_single_dict() -> None:
    """Tests the use case of a dictionary input with one key-value pair."""
    single_dict = {'cat': 'apple'}
    assert invert(single_dict) == {'apple': 'cat'}


def test_invert_normal_dict() -> None:
    """Tests the use case of a usual dictionary input."""
    normal_dict = {'Foluwa': 'Name:', '19' : 'Age:', 'Sophomore': 'Year:'}
    assert invert(normal_dict) == {'Name:': 'Foluwa', 'Age:': '19', 'Year:': 'Sophomore'}


def test_favorite_color_empty_dict() -> None:
    """Tests the edge case of an empty dict input."""
    empty_dict = {}
    assert favorite_color(empty_dict) == "No winner!"


def test_favorite_color_tied_dict() -> None:
    """Tests the use case of an dict input with two colors that appear at the same frequency."""
    tied_dict = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "John": "orange", "Will": "yellow"}
    assert favorite_color(tied_dict) == "yellow"


def test_favorite_color_winning_dict() -> None:
    """Tests the use case of a dict input with a clear wining color."""
    winning_dict = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(winning_dict) == "blue"


def test_count_empty_list() -> None:
    """Tests the edge case of an empty list input."""
    empty_list = list()
    assert count(empty_list) == {}


def test_count_tied_list() -> None:
    """Tests the use case of a list of strings with every string being seen with the same frequency."""
    tied_list: list[str] = count(["dog", "cat", "pig", "whale"])
    assert count(tied_list) == {"dog": 1, "cat": 1, "pig": 1, "whale": 1}


def test_count_ranked_list() -> None:
    """Tests the use case of a list of strings with every string being seen at a different frequency."""
    varied_list: list[str] = ["dog", "cat", "dog", "pig", "whale", "cat", "dog", "pig", "cat"]
    assert count(varied_list) == {"dog": 3, "cat": 3, "pig": 2, "whale": 1}