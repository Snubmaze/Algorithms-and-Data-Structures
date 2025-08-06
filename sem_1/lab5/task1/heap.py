import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[3]))

import os
from sem_1.utils.decorators import timer, memory_counter


PATH = os.path.dirname(__file__)
INPUT_FILE = f"{PATH}/input.txt"
OUTPUT_FILE = f"{PATH}/output.txt"


def is_heap(arr: list[int]) -> str:
    n = len(arr)
    for i in range(n):
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and arr[i] > arr[left]:
            return "NO"
        
        if right < n and arr[i] > arr[right]:
            return "YES"

    return "YES"


@timer
@memory_counter
def main():
    with open(INPUT_FILE) as f:
        n = int(f.readline())
        if not (1 <= n <= 10**5):
            raise ValueError("Неверные входные данные")

        arr = list(map(int, f.readline().split()))
        if len(arr) != n:
            raise ValueError("Неверные входные данные")

    result = is_heap(arr)

    with open(OUTPUT_FILE, 'w') as f:
        f.write(str(result))


if __name__ == "__main__":
    main()
