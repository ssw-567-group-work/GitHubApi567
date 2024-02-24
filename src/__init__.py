from .cli import Args


def main():
    args = Args(underscores_to_dashes=True).parse_args()


def add(a, b):
    return a + b
