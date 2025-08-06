import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[3]))

from sem_1.utils.decorators import timer, memory_counter
import os

PATH = os.path.dirname(__file__)
INPUT_FILE = f"{PATH}/input.txt"
OUTPUT_FILE = f"{PATH}/output.txt"


def rabin_karp(p: str, t: str) -> list[int]:
    result = []
    base = 256
    mod = 10**9 + 7
    m, n = len(p), len(t)

    if m > n:
        return result

    p_hash = 0
    t_hash = 0
    h = 1

    for _ in range(m - 1):
        h = (h * base) % mod

    for i in range(m):
        p_hash = (base * p_hash + ord(p[i])) % mod
        t_hash = (base * t_hash + ord(t[i])) % mod

    for i in range(n - m + 1):
        if p_hash == t_hash:
            if t[i:i + m] == p:
                result.append(i + 1)

        if i < n - m:
            t_hash = (base * (t_hash - ord(t[i]) * h) + ord(t[i + m])) % mod
            if t_hash < 0:
                t_hash += mod

    return result


@timer
@memory_counter
def main():
    with open(INPUT_FILE) as f:
        p = f.readline().strip()
        t = f.readline().strip()

    positions = rabin_karp(p, t)

    with open(OUTPUT_FILE, "w") as f:
        f.write(str(len(positions)) + "\n")
        if positions:
            f.write(" ".join(map(str, positions)) + "\n")


if __name__ == "__main__":
    main()
