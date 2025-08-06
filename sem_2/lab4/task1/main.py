import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[3]))

from sem_1.utils.decorators import timer, memory_counter
import os

PATH = os.path.dirname(__file__)
INPUT_FILE = f"{PATH}/input.txt"
OUTPUT_FILE = f"{PATH}/output.txt"


def naive_search(p: str, t: str) -> list[int]:
    m, n = len(p), len(t)
    result = []
    for i in range(n - m + 1):
        if t[i:i + m] == p:
            result.append(i + 1)
    return result


@timer
@memory_counter
def main():
    with open(INPUT_FILE) as f:
        p = f.readline().strip()
        t = f.readline().strip()

    positions = naive_search(p, t)

    with open(OUTPUT_FILE, "w") as f:
        f.write(str(len(positions)) + "\n")
        if positions:
            f.write(" ".join(map(str, positions)) + "\n")


if __name__ == "__main__":
    main()
