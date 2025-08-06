import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[3]))

from collections import deque
import os
from sem_1.utils.decorators import timer, memory_counter

PATH = os.path.dirname(__file__)
INPUT_FILE = f"{PATH}/input.txt"
OUTPUT_FILE = f"{PATH}/output.txt"


class MaxQueue:
    def __init__(self):
        self.data = deque()
        self.max_deque = deque()

    def push(self, value):
        self.data.append(value)
        while self.max_deque and self.max_deque[-1] < value:
            self.max_deque.pop()
        self.max_deque.append(value)

    def pop(self):
        if self.data:
            value = self.data.popleft()
            if value == self.max_deque[0]:
                self.max_deque.popleft()
            return value
        return None

    def max(self):
        return self.max_deque[0] if self.max_deque else None


@timer
@memory_counter
def main():
    with open(INPUT_FILE) as f:
        n = int(f.readline())
        if not (1 <= n <= 10**5):
            raise ValueError(f"n должно быть в диапазоне [1, 10^5], получено: {n}")

        arr = list(map(int, f.readline().split()))
        if len(arr) != n:
            raise ValueError(f"Длина массива должна быть равна n={n}, получено: {len(arr)}")

        for i, val in enumerate(arr):
            if not (0 <= val <= 10**5):
                raise ValueError(f"Элемент arr[{i}] = {val} вне диапазона [0, 10^5]")

        m = int(f.readline())
        if not (1 <= m <= n):
            raise ValueError(f"m должно быть в диапазоне [1, n={n}], получено: {m}")

    mq = MaxQueue()
    result = []

    for i in range(n):
        mq.push(arr[i])
        if i >= m - 1:
            result.append(mq.max())
            mq.pop()

    with open(OUTPUT_FILE, 'w') as f:
        f.write(' '.join(map(str, result)))


if __name__ == "__main__":
    main()
