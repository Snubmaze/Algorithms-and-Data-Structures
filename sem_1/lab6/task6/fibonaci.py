import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[3]))

from sem_1.utils.decorators import timer, memory_counter
import os


PATH = os.path.dirname(__file__)
INPUT_FILE = f"{PATH}/input.txt"
OUTPUT_FILE = f"{PATH}/output.txt"


def is_perfect_square(n: int) -> bool:
    if n < 0:
        return False
    left, right = 0, n
    while left <= right:
        mid = (left + right) // 2
        square = mid * mid
        if square == n:
            return True
        elif square < n:
            left = mid + 1
        else:
            right = mid - 1
    return False


def is_fib(n: int) -> bool:
    five_n2 = 5 * n * n
    return is_perfect_square(five_n2 + 4) or is_perfect_square(five_n2 - 4)


@timer
@memory_counter
def main():
    results = []

    with open(INPUT_FILE, encoding='utf-8') as f:
        N = int(f.readline())
        if not (1 <= N <= 10**6):
            raise ValueError("Неверные входные данные: N вне диапазона")
        
        lines = f.readlines()
        if len(lines) != N:
            raise ValueError("Несовпадение количества строк")
        
        for line in lines:
            num_str = line.strip()
            if len(num_str) > 5000:
                raise ValueError("Число превышает 5000 цифр")
            try:
                num = int(num_str)
            except ValueError:
                raise ValueError("Некорректное число во входе")

            result = "Yes" if is_fib(num) else "No"
            results.append(result)

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write('\n'.join(results) + '\n')


if __name__ == "__main__":
    main()
