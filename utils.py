import os

def get_filepath(filepath: str) -> str:
    return os.path.abspath(os.path.join(os.path.dirname(__file__), filepath))
    