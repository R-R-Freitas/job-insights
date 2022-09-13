from src.counter import count_ocurrences
# import pytest
path = "src/jobs.csv"
words = ["Python", "Javascript", "Parangaricutirimicuaro"]
results = [1639, 122, 0]
other_path = "tests/mocks/jobs.csv"
more_words = ["Full", "Developer", "End"]
more_results = [3, 3, 3]


def test_counter():
    for index in range(len(words)):
        result = count_ocurrences(path, words[index])
        assert result == results[index]
    for index in range(len(more_words)):
        result = count_ocurrences(other_path, more_words[index])
        assert result == more_results[index]


test_counter()
