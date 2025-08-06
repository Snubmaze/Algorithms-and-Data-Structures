import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[3]))

from sem_1.utils.decorators import timer, memory_counter
import os


PATH = os.path.dirname(__file__)
INPUT_FILE = f"{PATH}/input.txt"
OUTPUT_FILE = f"{PATH}/output.txt"


class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, N):
        self.items.append(N)

    def delete(self):
        self.items.pop()
    
    def view_el(self):
        try:
            return self.items[-1]
        except IndexError:
            return None
    

def is_good(seq: str) -> bool:
    if len(seq) % 2 != 0:
        return False

    stack = Stack()
    pairs = {"(": ")", "[": "]"}

    for brack in seq:
        if brack in pairs:
            stack.push(brack)
        else:
            top = stack.view_el()
            if top is None or pairs[top] != brack:
                return False
            stack.delete()
    
    return stack.view_el() is None
    
    

@timer
@memory_counter
def main():
    with open(INPUT_FILE) as f:
        N = int(f.readline())
        if not 1 <= N <= 500:
            raise ValueError("Неверные входные данные")
        
        seq_arr = [f.readline().strip() for _ in range(N)]

    with open(OUTPUT_FILE, 'w') as f:
        for seq in seq_arr:
            result = is_good(seq)
            if result:
                f.write("YES\n")
            else:
                f.write("NO\n")


if __name__ == '__main__':
    main()