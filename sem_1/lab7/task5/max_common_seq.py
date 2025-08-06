import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[3]))

from sem_1.utils.decorators import timer, memory_counter
import os


PATH = os.path.dirname(__file__)
INPUT_FILE = f"{PATH}/input.txt"
OUTPUT_FILE = f"{PATH}/output.txt"


def get_max_common_seq_of_three(a, b, c):
    n, m, l = len(a), len(b), len(c)
    dp = [[[0] * (l + 1) for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(n):
        for j in range(m):
            for k in range(l):
                if a[i] == b[j] == c[k]:
                    dp[i + 1][j + 1][k + 1] = dp[i][j][k] + 1
                else:
                    dp[i + 1][j + 1][k + 1] = max(
                        dp[i][j + 1][k + 1],
                        dp[i + 1][j][k + 1],
                        dp[i + 1][j + 1][k]
                    )
    return dp[n][m][l]


@timer
@memory_counter
def main():
    with open(INPUT_FILE) as f:
        n = int(f.readline())
        if not (1 <= n <= 100):
            raise ValueError("Неверные входные данные")
        A = list(map(int, f.readline().strip().split()))
        if len(A) != n:
            raise ValueError("Несовпадение количества элементов в A")

        m = int(f.readline())
        if not (1 <= m <= 100):
            raise ValueError("Неверные входные данные")
        B = list(map(int, f.readline().strip().split()))
        if len(B) != m:
            raise ValueError("Несовпадение количества элементов в B")

        l = int(f.readline())
        if not (1 <= l <= 100):
            raise ValueError("Неверные входные данные")
        C = list(map(int, f.readline().strip().split()))
        if len(C) != l:
            raise ValueError("Несовпадение количества элементов в C")

        if any(abs(x) >= 10**9 for x in A + B + C):
            raise ValueError("Неверные значения элементов")

    result = get_max_common_seq_of_three(A, B, C)

    with open(OUTPUT_FILE, 'w') as f:
        f.write(str(result))




if __name__ == "__main__":
    main()
