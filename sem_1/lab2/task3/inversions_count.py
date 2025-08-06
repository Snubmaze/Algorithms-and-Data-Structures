import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[3]))

from sem_1.utils.decorators import timer, memory_counter
import os


PATH = os.path.dirname(__file__)
INPUT_FILE = f"{PATH}/input.txt"
OUTPUT_FILE = f"{PATH}/output.txt"


def count_inversions(arr):
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr, 0

        mid = len(arr) // 2
        left, inv_left = merge_sort(arr[:mid])
        right, inv_right = merge_sort(arr[mid:])
        merged, inv_merge = merge(left, right)

        total_inversions = inv_left + inv_right + inv_merge
        return merged, total_inversions

    def merge(left, right):
        merged = []
        i = j = inv_count = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                inv_count += len(left) - i
                j += 1

        merged += left[i:]
        merged += right[j:]
        return merged, inv_count

    _, total_inversions = merge_sort(arr)
    return total_inversions


@timer
@memory_counter
def main():
    with open(INPUT_FILE, 'r') as f:
        n = int(f.readline())
        arr = list(map(int, f.readline().split()))
    
    if (1 <= n <= 2 * 10 ** 5) and (n == len(arr)) and (all(abs(i) <= 10**9 for i in arr)):
        result = str(count_inversions(arr))

        with open(OUTPUT_FILE, 'w') as f:
            f.write(result)

    else:
        print("Неверные входные данные")


if __name__ == "__main__":
    main()