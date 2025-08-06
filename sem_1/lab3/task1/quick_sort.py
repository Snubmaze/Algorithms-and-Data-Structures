import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[3]))

from sem_1.utils.decorators import timer, memory_counter
from sem_1.lab1.task1.insertion import insertion_sort
import os
import random


PATH = os.path.dirname(__file__)
INPUT_FILE = f"{PATH}/input.txt"
OUTPUT_FILE = f"{PATH}/output.txt"


def default_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    key = arr[len(arr) // 2]
    left = [i for i in arr[1:] if i < key]
    right = [i for i in arr[1:] if i >= key]

    return default_quick_sort(left) + [key] + default_quick_sort(right)
        

def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr

    while True:
        key = random.choice(arr)
        if any(x != key for x in arr):
            break
        else:
            return arr

    left = [x for x in arr if x < key]
    right = [x for x in arr if x >= key]

    return randomized_quick_sort(left) + randomized_quick_sort(right)


def three_parts_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    key = random.choice(arr)
    left = [i for i in arr if i < key]
    mid  = [i for i in arr if i == key]
    right = [i for i in arr if i > key]

    return three_parts_quick_sort(left) + mid + three_parts_quick_sort(right)


def case_compare_task1():
    
    @timer
    def run_randomized_quick_sort(case):
        randomized_quick_sort(case)
            
    @timer
    def run_default_quick_sort(case):
        default_quick_sort(case)
    
    
    def worst_case_compare():
        n = 10**3
        worst_case = list(range(10**9, 10**9 - n, -1))

        print("Randomized-QuickSort:")
        run_randomized_quick_sort(worst_case)

        print("\nDefault QuickSort:")
        run_default_quick_sort(worst_case)


    def best_case_compare():
        n = 10**3
        best_case = list(range(10**9 - n, 10**9))

        print("Randomized-QuickSort:")
        run_randomized_quick_sort(best_case)

        print("\nDefault QuickSort:")
        run_default_quick_sort(best_case)


    def middle_case_compare():
        n = 10**3
        middle_case = (list(range(10**9 - n, 10**9)))
        random.shuffle(middle_case)

        print("Randomized-QuickSort:")
        run_randomized_quick_sort(middle_case)

        print("\nDefault QuickSort:")
        run_default_quick_sort(middle_case)


    print("_________________________________")
    print("\nWorst case:\n")
    worst_case_compare()
    print("_________________________________")

    print("\nMiddle case:\n")
    middle_case_compare()
    print("_________________________________")
    
    print("\nBest case:\n")
    best_case_compare()
    print("_________________________________")


def case_compare_task2():
    
    @timer
    def run_randomized_quick_sort(case):
        randomized_quick_sort(case)
            
    @timer
    def run_three_parts_quick_sort(case):
        three_parts_quick_sort(case)
    
    
    def worst_case_compare():
        n = 10**3
        worst_case = list(range(10**9, 10**9 - n, -1))

        print("Randomized-QuickSort:")
        run_randomized_quick_sort(worst_case)

        print("\nThree-Partition-QuickSort:")
        run_three_parts_quick_sort(worst_case)


    def best_case_compare():
        n = 10**3
        best_case = list(range(10**9 - n, 10**9))

        print("Randomized-QuickSort:")
        run_randomized_quick_sort(best_case)

        print("\nThree-Partition-QuickSort:")
        run_three_parts_quick_sort(best_case)


    def middle_case_compare():
        n = 10**3
        middle_case = (list(range(10**9 - n, 10**9)))
        random.shuffle(middle_case)

        print("Randomized-QuickSort:")
        run_randomized_quick_sort(middle_case)

        print("\nThree-Partition-QuickSort:")
        run_three_parts_quick_sort(middle_case)


    print("_________________________________")
    print("\nWorst case:\n")
    worst_case_compare()
    print("_________________________________")

    print("\nMiddle case:\n")
    middle_case_compare()
    print("_________________________________")
    
    print("\nBest case:\n")
    best_case_compare()
    print("_________________________________")


@timer
@memory_counter
def main():
    with open(INPUT_FILE, 'r') as f:
        n = int(f.readline())
        arr = list(map(int, f.readline().split()))
    
    if (1 <= n <= 2 * 10 ** 4) and (n == len(arr)) and (all(abs(i) <= 10**9 for i in arr)):
        
        result_task1 = ", ".join(map(str, randomized_quick_sort(arr)))
        with open(f"{PATH}/output_task1.txt", 'w') as f:
            f.write(result_task1)
        
        print("\nCompare Randomized-QuickSort and Default-QuickSort:\n")
        case_compare_task1()

        result_task2 = ", ".join(map(str, three_parts_quick_sort(arr)))
        with open(f"{PATH}/output_task2.txt", 'w') as f:
            f.write(result_task2)

        print("\n################################################################\n")
        print("\nCompare Randomized-QuickSort and Three-Partition-QuickSort:\n")
        case_compare_task2()

    else:
        print("Неверные входные данные")


if __name__ == '__main__':
    main()