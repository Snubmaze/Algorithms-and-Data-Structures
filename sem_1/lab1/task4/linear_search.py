import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[3]))

from sem_1.utils.decorators import timer
import os


PATH = os.path.dirname(__file__)


def linear_search(arr: list[int], n: int) -> int:
    result = []
    for i in range(len(arr)):
        if arr[i] == n:
            result.append(i)
    return result if len(result) else -1
    
@timer
def main():
    with open(f"{PATH}/input.txt", 'r') as f:
        arr = [i for i in map(int, f.readline().split(" "))]
        n = int(f.readline())
    
    if any(abs(i) > 10**3 for i in arr) or not (0 <= len(arr) <= 10**3):
        print("Неверные входные данные")
    
    else:
        result = linear_search(arr, n)
        
        with open(f"{PATH}/output.txt", 'w') as f:
            if result == -1:
                f.write("-1")
            else:
                f.write(str(len(result)))
                f.write("\n")
                f.write(", ".join(map(str, result)))

if __name__ == '__main__':
    main()