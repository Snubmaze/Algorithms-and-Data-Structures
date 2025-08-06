import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[3]))

from sem_1.utils.decorators import timer, memory_counter
import os

PATH = os.path.dirname(__file__)
INPUT_FILE = f"{PATH}/input.txt"
OUTPUT_FILE = f"{PATH}/output.txt"


def compress_string(s: str) -> str:
    n = len(s)
    dp = [[""] * (n + 1) for _ in range(n + 1)]

    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length
            substr = s[i:j]

            dp[i][j] = substr

            for k in range(i + 1, j):
                left = dp[i][k]
                right = dp[k][j]
                candidate = left + "+" + right
                if len(candidate) < len(dp[i][j]):
                    dp[i][j] = candidate

            for block_len in range(1, length // 2 + 1):
                if length % block_len == 0:
                    times = length // block_len
                    block = substr[:block_len]
                    if block * times == substr:
                        compressed_block = dp[i][i + block_len]
                        if times == 1:
                            rep = compressed_block
                        else:
                            rep = f"{compressed_block}*{times}"
                        if len(rep) < len(dp[i][j]):
                            dp[i][j] = rep

    return dp[0][n]


@timer
@memory_counter
def main():
    with open(INPUT_FILE) as f:
        s = f.readline().strip()

    result = compress_string(s)

    with open(OUTPUT_FILE, "w") as f:
        f.write(result + "\n")


if __name__ == "__main__":
    main()
