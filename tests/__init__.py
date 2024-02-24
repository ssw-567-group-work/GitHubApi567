import os


def read_fixture(resource: str) -> str:
    path = os.path.dirname(__file__)
    with open(f"{path}/fixtures/{resource}", "r") as f:
        return f.read()
