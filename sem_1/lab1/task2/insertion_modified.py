import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[3]))

from sem_1.utils.decorators import timer
from sem_1.utils.validators  import validate_length, validate_numbers
from sem_1.utils.io_utils import read_ints, write_output
from sem_1.lab1.task1.insertion import insertion_sort
import os


PATH = os.path.dirname(__file__)


def insertion_sort_positions(arr):
    n = len(arr)
    positions = [0] * n
    result = arr[:]
    for i in range(1, n):
        key = result[i]
        j = i - 1
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = key
        positions[i] = j + 1

    positions[0] = 0

    positions = [p + 1 for p in positions]
    return positions


@timer
def main():
    n, arr = read_ints(PATH)
    length_check = validate_length(n, arr)
    numbers_range_check = validate_numbers(arr)

    if length_check and numbers_range_check:
        positions = insertion_sort_positions(arr)
        write_output(PATH, positions)
    else:
        print("[ERROR] : Неверные входные данные")


if __name__ == '__main__':
    main()
