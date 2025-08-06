import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[3]))

from sem_1.utils.decorators import timer, memory_counter
import os


PATH = os.path.dirname(__file__)
INPUT_FILE = f"{PATH}/input.txt"
OUTPUT_FILE = f"{PATH}/output.txt"


def get_max_items(items: list[tuple], W: int) -> float:
    items.sort(key=lambda x: x[0] / x[1], reverse=True)
    total_value = 0.0
    for value, weight in items:
        if W == 0:
            break
        if weight <= W:
            total_value += value
            W -= weight
        else:
            fraction = W / weight
            total_value += value * fraction
            break

    return round(total_value, 4)
    

@timer
@memory_counter
def main():
    with open(INPUT_FILE) as f:
        n, W = map(int, f.readline().strip().split())
        if not (1 <= n <= 10**3 and 0 <= W <= 2 * 10**6):
            raise ValueError("Неверные входные данные")
        
        items = []

        for _ in range(n):
            value, weight = map(int, f.readline().strip().split())
            
            if not(0 <= weight <= 20 * 10**6 and 0 <= value <= 2 * 10**6):
                raise ValueError("Неверные входные данные")
            
            items.append((value, weight))

    result = get_max_items(items, W)
    
    with open(OUTPUT_FILE, 'w') as f:
        f.write(str(result))


if __name__ == "__main__":
    main()