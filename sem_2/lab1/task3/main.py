import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[3]))

from sem_1.utils.decorators import timer, memory_counter
import os


PATH = os.path.dirname(__file__)
INPUT_FILE = f"{PATH}/input.txt"
OUTPUT_FILE = f"{PATH}/output.txt"


def max_dot_product(A, B):

    A.sort(reverse=True)
    B.sort(reverse=True)

    result = sum(x * y for x, y in zip(A, B))
    return result


@timer
@memory_counter
def main():
    with open(INPUT_FILE) as f:
        n = int(f.readline())
        if not 1 <= n <= 10**3:
            raise ValueError("Неверные входные данные")
        
        A = list(map(int, f.readline().strip().split()))
        B = list(map(int, f.readline().strip().split()))
        if any([abs(a) >= 10**5 for a in A]) or any([abs(b) >= 10**5 for b in B]):
               raise ValueError("Неверные входные данные")

    result = max_dot_product(A, B)
    
    with open(OUTPUT_FILE, 'w') as f:
        f.write(str(result))


if __name__ == "__main__":
    main()