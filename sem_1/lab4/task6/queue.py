import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[3]))

from sem_1.utils.decorators import timer, memory_counter
import os


PATH = os.path.dirname(__file__)
INPUT_FILE = f"{PATH}/input.txt"
OUTPUT_FILE = f"{PATH}/output.txt"


class Queue:
    def __init__(self):
        self.items = []
    
    def push(self, el):
        self.items.append(el)

    def get_min(self):
        el = min(self.items)
        return str(el)
    
    def get(self):
        el = self.items[0]
        self.items.remove(el)


@timer
@memory_counter
def main():
    queue = Queue()
    results = []

    with open(INPUT_FILE) as f:
        M = int(f.readline())
        if not 1 <= M <= 10**6:
            raise ValueError("Неверные входные данные")

        commands = [command.strip() for command in f.readlines()]
        if len(commands) != M:
            raise ValueError("Неверные входные данные")

    for command in commands:
        if command[0] == '+':
            N = int(command[1:].strip())
            
            if not abs(N) <= 10**9:
                raise ValueError("Неверные входные данные")
            
            queue.push(N)

        elif command[0] == '-':
            queue.get()

        elif command[0] == '?':
            results.append(queue.get_min())
        
        else:
            print("Неизвестная операция")

    with open(OUTPUT_FILE, 'w') as f:
        for result in results:
            f.write(f"{result}\n")


if __name__ == "__main__":
    main()