"""Unit Tests for EX05 functions."""

__author__ = "730480375"


from utils import only_evens, concat, sub


def test_only_evens_empty_list() -> None:
    """Tests the edge case of an empty list input."""
    empty_list: list[int] = list()
    assert only_evens(empty_list) == []


def test_only_evens_odd_list() -> None:
    """Tests the use case of a list input with only odd numbers."""
    odd_list: list[int] = [3, 5, 9, 7, 1]
    assert only_evens(odd_list) == []


def test_only_evens_normal_list() -> None:
    """Tests the use case of a list of ints with some odd and even numbers."""
    normal_list: list[int] = [0, 1, 2, 5, 7, 4, 6]
    assert only_evens(normal_list) == [0, 2, 4, 6]


def test_concat_empty_first_list() -> None:
    """Tests the edge case of the first list being empty."""
    empty_list: list[int] = list()
    normal_list: list[int] = [3, 4, 1, 2]
    assert concat(empty_list, normal_list) == [3, 4, 1, 2]


def test_concat_same_list_lengths() -> None:
    """Tests the use case of two lists of ints of the same length."""
    list_1: list[int] = [3, 1, 4, 2]
    list_2: list[int] = [5, 8, 6, 7]
    assert concat(list_1, list_2) == [3, 1, 4, 2, 5, 8, 6, 7]


def test_concat_different_list_lengths() -> None:
    """Tests the use case of two lists of ints with different lengths."""
    list_1: list[int] = [3, 1, 2, 4]
    list_2: list[int] = [5, 8, 7]
    assert concat(list_1, list_2) == [3, 1, 2, 4, 5, 8, 7]


def test_sub_empty_list() -> None:
    """Tests the edge case of an empty list."""
    empty_list: list[int] = list()
    assert sub(empty_list, 1, 3) == []


def test_sub_short_list() -> None:
    """Tests the use case of a short list input."""
    short_list: list[int] = [10, 20, 30]
    assert sub(short_list, 1, 3) == [20, 30]


def test_sub_long_list() -> None:
    """Tests the use case of a longer list input (e.g, > 4 ints)."""
    long_list: list[int] = [10, 6, 4, 2, 8, 9, 5]
    assert sub(long_list, 1, 5) == [6, 4, 2, 8]