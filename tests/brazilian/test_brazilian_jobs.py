from src.brazilian_jobs import read_brazilian_file


path = "tests/mocks/brazilians_jobs.csv"
keys = ["title", "salary", "type"]


def test_brazilian_jobs():
    jobs = read_brazilian_file(path)
    for job in jobs:
        for key in keys:
            assert key in job.keys()
