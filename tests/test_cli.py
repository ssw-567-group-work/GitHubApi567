from src.cli import Args
import pytest


def test_cli_args():
    args = Args(underscores_to_dashes=True).parse_args(["dyc3"])
    assert args.username == "dyc3"

    with pytest.raises(ValueError):
        args = Args(underscores_to_dashes=True).parse_args([""])
