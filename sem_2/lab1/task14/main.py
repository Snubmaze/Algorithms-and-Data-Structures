import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[3]))

from sem_1.utils.decorators import timer, memory_counter
import os


PATH = os.path.dirname(__file__)
INPUT_FILE = f"{PATH}/input.txt"
OUTPUT_FILE = f"{PATH}/output.txt"


def eval_op(a: int, b: int, op: str) -> int:
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b


def get_max_result(nums: list[int], symbols: list[str]) -> int:
    n = len(nums)
    dp_min = [[0] * n for _ in range(n)]
    dp_max = [[0] * n for _ in range(n)]

    for i in range(n):
        dp_min[i][i] = dp_max[i][i] = nums[i]

    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            min_val = float('inf')
            max_val = float('-inf')
            for k in range(i, j):
                op = symbols[k]

                a = eval_op(dp_max[i][k], dp_max[k + 1][j], op)
                b = eval_op(dp_max[i][k], dp_min[k + 1][j], op)
                c = eval_op(dp_min[i][k], dp_max[k + 1][j], op)
                d = eval_op(dp_min[i][k], dp_min[k + 1][j], op)

                min_val = min(min_val, a, b, c, d)
                max_val = max(max_val, a, b, c, d)

            dp_min[i][j] = min_val
            dp_max[i][j] = max_val

    return dp_max[0][n - 1]



@timer
@memory_counter
def main():
    with open(INPUT_FILE) as f:
        s = f.readline()
        if len(s) > 29:
            raise ValueError("Неверные входные данные")

        try:
            nums = list(map(int, s[::2]))
        except Exception:
            raise ValueError("Неверные входные данные")
        
        symbols = [s[i] for i in range(1, len(s), 2)]

    result = get_max_result(nums, symbols)
            
    with open(OUTPUT_FILE, 'w') as f:
        f.write(str(result))


if __name__ == "__main__":
    main()