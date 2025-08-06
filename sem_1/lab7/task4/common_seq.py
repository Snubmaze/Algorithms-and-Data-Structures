import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[3]))

from sem_1.utils.decorators import timer, memory_counter
import os


PATH = os.path.dirname(__file__)
INPUT_FILE = f"{PATH}/input.txt"
OUTPUT_FILE = f"{PATH}/output.txt"


def get_max_seq_len(A: list, B: list) -> int:
    n = len(A)
    m = len(B)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n):
        for j in range(m):
            if A[i] == B[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

    return dp[n][m]


@timer
@memory_counter
def main():
    with open(INPUT_FILE) as f:
        n = int(f.readline())
        if not (1 <= n <= 100):
            raise ValueError("Неверные входные данные")
        
        A = list(map(int, f.readline().strip().split()))
        print(A)
        if len(A) != n:
            raise ValueError("Несовпадение количества строк")
        
        m = int(f.readline())
        if not (1 <= m <= 100):
            raise ValueError("Неверные входные данные")
        
        B = list(map(int, f.readline().strip().split()))
        if len(B) != m:
            raise ValueError("Несовпадение количества строк")

        if any([abs(a) >= 10**9 for a in A]) or any([abs(b) >= 10**9 for b in B]):
            raise ValueError("Неверные входные данные")
    
    result = get_max_seq_len(A, B)

    with open(OUTPUT_FILE, 'w') as f:
        f.write(str(result))


if __name__ == "__main__":
    main()
