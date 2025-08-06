import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[3]))

from sem_1.utils.decorators import timer
from sem_1.utils.validators  import validate_length, validate_numbers
from sem_1.utils.io_utils import read_ints, write_output
import os


PATH = os.path.dirname(__file__)


def insertion_sort(arr: list[int]) -> list[int]:
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = key
    return arr


@timer
def main():
    n, arr = read_ints(PATH)

    length_check = validate_length(n, arr)
    numbers_range_check = validate_numbers(arr)

    if length_check and numbers_range_check:
        sorted_arr = insertion_sort(arr)
        write_output(PATH, sorted_arr)

    else:
        print("Неверные входные данные")


if __name__ == '__main__':
    main()
