# sem_1/utils/path_utils.py
from pathlib import Path

def get_data_path(filename: str) -> str:
    # путь к папке, где лежит этот скрипт
    return str(Path(__file__).parent.parent / filename)
