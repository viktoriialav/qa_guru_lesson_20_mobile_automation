import selene_in_action
from pathlib import Path


def abs_path_from_root(path: str):
    return Path(selene_in_action.__file__).parent.parent.joinpath(path).absolute().__str__()
