import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[3]))

from sem_1.utils.decorators import timer, memory_counter
import os
import random


PATH = os.path.dirname(__file__)
INPUT_FILE = f"{PATH}/input.txt"
OUTPUT_FILE = f"{PATH}/output.txt"


def radix_sort(columns: list[str], k: int) -> list[int]:
    order = None

    for phase in range(k):
        current_column = columns[phase]
        pos_to_char = {i + 1: current_column[i] for i in range(len(current_column))}

        if order is None:
            sorted_items = sorted(pos_to_char.items(), key=lambda item: ord(item[1]))
            order = [pos for pos, _ in sorted_items]
        else:
            ordered_chars = [(pos, ord(pos_to_char[pos])) for pos in order]
            ordered_chars.sort(key=lambda item: item[1])
            order = [pos for pos, _ in ordered_chars]

    return order


@timer
@memory_counter
def main():
    with open(INPUT_FILE) as f:
        st = []
        n, m, k = map(int, f.readline().split())
        for line in reversed(f.readlines()[-k:]):
            st.append(line.replace('\n', ''))
        
    if not 1 <= n <= 10**6 or not 1 <= k <= m <= 10**6 or not n * m <= 5 * 10**7:
        raise ValueError("Неверные входные данные")
    
    result = radix_sort(st, k)

    with open(OUTPUT_FILE, 'w') as f:
        f.write(''.join(map(str, result)))
    

if __name__ == '__main__':
    main()