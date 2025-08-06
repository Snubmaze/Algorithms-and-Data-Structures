import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[3]))

from sem_1.utils.decorators import timer, memory_counter
from sem_1.utils.validators  import validate_length, validate_numbers
from sem_1.utils.io_utils import read_ints, write_output
from sem_1.lab1.task1.insertion import insertion_sort
import os
import random

PATH = os.path.dirname(__file__)
INPUT_FILE = f"{PATH}/input.txt"
OUTPUT_FILE = f"{PATH}/output.txt"


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Задание 1
@timer
@memory_counter
def main():
    with open(INPUT_FILE, 'r') as f:
        n = int(f.readline())
        arr = list(map(int, f.readline().split()))
    
    if (1 <= n <= 2 * 10 ** 4) and (n == len(arr)) and (all(abs(i) <= 10**9 for i in arr)):
        result = ", ".join(map(str, merge_sort(arr)))

        with open(OUTPUT_FILE, 'w') as f:
            f.write(result)

    else:
        print("Неверные входные данные")


# Задание 2 - сравниваем слияние и втсавку для худшего случая
def case_compare():
    
    @timer
    def run_merge_sort(case):
        merge_sort(case)
            
    @timer
    def run_insertion_sort(case):
        insertion_sort(case)
    
    
    def worst_case_compare():
        n = 10**3
        worst_case = list(range(10**9, 10**9 - n, -1))

        print("Merging sort:")
        run_merge_sort(worst_case)

        print("\nInsertion sort:")
        run_insertion_sort(worst_case)


    def best_case_compare():
        n = 10**3
        best_case = list(range(10**9 - n, 10**9))

        print("Merging sort:")
        run_merge_sort(best_case)

        print("\nInsertion sort:")
        run_insertion_sort(best_case)

    def middle_case_compare():
        n = 10**3
        middle_case = (list(range(10**9 - n, 10**9)))
        random.shuffle(middle_case)

        print("Merging sort:")
        run_merge_sort(middle_case)

        print("\nInsertion sort:")
        run_insertion_sort(middle_case)


    print("Worst case:\n")
    worst_case_compare()
    print("_________________________________")

    print("\nMiddle case:\n")
    middle_case_compare()
    print("_________________________________")
    
    print("\nBest case:\n")
    best_case_compare()
    print("_________________________________")



if __name__ == '__main__':
    main()
    print("##########################################")
    print("Compare sortings in different cases:\n")
    case_compare()