from src.counter import count_ocurrences
# import pytest
path = "src/jobs.csv"
words = ["Python", "Javascript", "Parangaricutirimicuaro"]
results = [1639, 122, 0]


def test_counter():
    for index in range(len(words)):
        result = count_ocurrences(path, words[index])
        assert result == results[index]


test_counter()
