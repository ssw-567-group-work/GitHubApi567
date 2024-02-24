from .cli import Args
from .fetcher import Fetcher


def main():
    args = Args(underscores_to_dashes=True).parse_args()
    fetcher = Fetcher()
    # TODO: implement


def add(a, b):
    return a + b
