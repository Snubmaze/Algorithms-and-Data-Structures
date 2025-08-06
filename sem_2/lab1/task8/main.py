import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[3]))

from sem_1.utils.decorators import timer, memory_counter
import os


PATH = os.path.dirname(__file__)
INPUT_FILE = f"{PATH}/input.txt"
OUTPUT_FILE = f"{PATH}/output.txt"


def get_max_lectures(lectures):
    lectures.sort(key=lambda x: x[1])

    count = 0
    last_end = 0

    for start, end in lectures:
        if start >= last_end:
            count += 1
            last_end = end

    return count


@timer
@memory_counter
def main():
    with open(INPUT_FILE) as f:
        N = int(f.readline())
        if not 1 <= N <= 10**3:
            raise ValueError("Неверные входные данные")
        
        lectures = []
        
        for _ in range(N):
            st, end = list(map(int, f.readline().strip().split()))
            if not 1 <= st < end <= 1440:
                raise ValueError("Неверные входные данные")
            lectures.append([st, end])
        
        result = get_max_lectures(lectures)
            
    with open(OUTPUT_FILE, 'w') as f:
        f.write(str(result))


if __name__ == "__main__":
    main()