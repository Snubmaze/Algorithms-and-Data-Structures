import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[3]))

from sem_1.utils.decorators import timer, memory_counter
import os


PATH = os.path.dirname(__file__)
INPUT_FILE = f"{PATH}/input.txt"
OUTPUT_FILE = f"{PATH}/output.txt"


knight_moves = {
        0: [4, 6],
        1: [6, 8],
        2: [7, 9],
        3: [4, 8],
        4: [0, 3, 9],
        5: [],
        6: [0, 1, 7],
        7: [2, 6],
        8: [1, 3],
        9: [2, 4],
    }


def get_knight_numbers_count(N: int) -> int:
    if N == 0:
        return 0

    dp = [[0] * 10 for _ in range(N + 1)]

    for d in range(10):
        if d != 0 and d != 8:
            dp[1][d] = 1

    for i in range(2, N + 1):
        for d in range(10):
            for prev in knight_moves[d]:
                dp[i][d] = (dp[i][d] + dp[i - 1][prev]) % 10**9

    return sum(dp[N]) % 10**9
    

@timer
@memory_counter
def main():
    with open(INPUT_FILE) as f:
        N = int(f.readline())
        if not 1 <= N <= 1000:
            raise ValueError("Неверные входные данные")

    result = get_knight_numbers_count(N)
            
    with open(OUTPUT_FILE, 'w') as f:
        f.write(str(result))


if __name__ == "__main__":
    main()