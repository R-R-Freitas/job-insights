from src.sorting import sort_by
import pytest


@pytest.fixture
def mock_file():
    return [
        {
            "title": "Web developer",
            "min_salary": "",
            "max_salary": "",
            "date_posted": "2020-05-08",
        },
        {
            "title": "Front end developer",
            "min_salary": "1000",
            "max_salary": "",
            "date_posted": "2020-06-07",
        },
        {
            "title": "Back end developer",
            "min_salary": "",
            "max_salary": "3000",
            "date_posted": "Invalid date",
        },
        {
            "title": "Full stack end developer",
            "min_salary": "4000",
            "max_salary": "8000",
            "date_posted": "2019-10-11",
        },
    ]


mock_min_salary_result = [
    {
        "title": "Front end developer",
        "min_salary": "1000",
        "max_salary": "",
        "date_posted": "2020-06-07",
    },
    {
        "title": "Full stack end developer",
        "min_salary": "4000",
        "max_salary": "8000",
        "date_posted": "2019-10-11",
    },
    {
        "title": "Web developer",
        "min_salary": "",
        "max_salary": "",
        "date_posted": "2020-05-08",
    },
    {
        "title": "Back end developer",
        "min_salary": "",
        "max_salary": "3000",
        "date_posted": "Invalid date",
    },
]

mock_max_salary_result = [
    {
        "title": "Full stack end developer",
        "min_salary": "4000",
        "max_salary": "8000",
        "date_posted": "2019-10-11",
    },
    {
        "title": "Back end developer",
        "min_salary": "",
        "max_salary": "3000",
        "date_posted": "Invalid date",
    },
    {
        "title": "Web developer",
        "min_salary": "",
        "max_salary": "",
        "date_posted": "2020-05-08",
    },
    {
        "title": "Front end developer",
        "min_salary": "1000",
        "max_salary": "",
        "date_posted": "2020-06-07",
    },
]

mock_date_posted_result = [
    {
        "title": "Front end developer",
        "min_salary": "1000",
        "max_salary": "",
        "date_posted": "2020-06-07",
    },
    {
        "title": "Web developer",
        "min_salary": "",
        "max_salary": "",
        "date_posted": "2020-05-08",
    },
    {
        "title": "Full stack end developer",
        "min_salary": "4000",
        "max_salary": "8000",
        "date_posted": "2019-10-11",
    },
    {
        "title": "Back end developer",
        "min_salary": "",
        "max_salary": "3000",
        "date_posted": "Invalid date",
    },
]

min = "min_salary"
max = "max_salary"
date_posted = "date_posted"


def assert_sort_by_max_salary(result):
    try:
        for index in range(len(result)):
            if max in result[index].keys():
                job_key = result[index][max]
                expected_job_key = mock_max_salary_result[index][max]
                assert job_key == expected_job_key
            else:
                assert max not in mock_max_salary_result[index].keys()
    except TypeError:
        raise TypeError("invalid result")


def assert_sort_by_min_salary(result):
    try:
        for index in range(len(result)):
            if min in result[index].keys():
                job_key = result[index][min]
                expected_job_key = mock_min_salary_result[index][min]
                assert job_key == expected_job_key
            else:
                assert min not in mock_min_salary_result[index].keys()
    except TypeError:
        raise TypeError("invalid result")


def assert_sort_by_date_posted(result):
    try:
        for index in range(len(result)):
            if date_posted in result[index].keys():
                job_key = result[index][date_posted]
                expected_job_key = mock_date_posted_result[index][date_posted]
                assert job_key == expected_job_key
            else:
                assert date_posted not in mock_date_posted_result[index].keys()
    except TypeError:
        raise TypeError("invalid result")


def test_sort_by_criteria(mock_file):
    try:
        result = sort_by(mock_file, max)
        assert result is not None
        assert_sort_by_max_salary(result)
        result = sort_by(mock_file, min)
        assert result is not None
        assert_sort_by_min_salary(result)
        result = sort_by(mock_file, date_posted)
        assert_sort_by_date_posted(result)
    except AssertionError:
        raise AssertionError("invalid result")
