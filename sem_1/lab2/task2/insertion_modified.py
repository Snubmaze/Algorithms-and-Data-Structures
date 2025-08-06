import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[3]))

from sem_1.utils.decorators import timer, memory_counter
import os

PATH = os.path.dirname(__file__)
INPUT_FILE = f"{PATH}/input.txt"
OUTPUT_FILE = f"{PATH}/output.txt"


def merge_sort(arr, left, right, original_indices, output):
    if left >= right:
        return

    mid = (left + right) // 2

    merge_sort(arr, left, mid, original_indices, output)
    merge_sort(arr, mid + 1, right, original_indices, output)

    temp = []
    i, j = left, mid + 1

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    while i <= mid:
        temp.append(arr[i])
        i += 1
    while j <= right:
        temp.append(arr[j])
        j += 1

    for i in range(left, right + 1):
        arr[i] = temp[i - left]

    If = original_indices[left] + 1
    Il = original_indices[right] + 1
    Vf = arr[left]
    Vl = arr[right]
    output.append(f"{If} {Il} {Vf} {Vl}") 


@timer
@memory_counter
def main():
    with open(INPUT_FILE) as f:
        n = int(f.readline())
        arr = list(map(int, f.readline().split()))

    if (1 <= n <= 10 ** 5) and (n == len(arr)) and (all(abs(i) <= 10**9 for i in arr)):
        original_indices = list(range(n))

        output = []

        merge_sort(arr, 0, n - 1, original_indices, output)

        with open(OUTPUT_FILE, 'w') as f:
            for line in output:
                f.write(line + '\n')
            f.write(' '.join(map(str, arr)) + '\n')
    else:
        print("Неверные входные данные")


if __name__ == "__main__":
    main()
