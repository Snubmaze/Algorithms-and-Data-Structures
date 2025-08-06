import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[3]))

from sem_1.utils.decorators import timer, memory_counter
import os


PATH = os.path.dirname(__file__)
INPUT_FILE = f"{PATH}/input.txt"
OUTPUT_FILE = f"{PATH}/output.txt"


class Set:
    def __init__(self):
        self.items = []
    
    def is_added(self, N):
        return "Y" if N in self.items else "N"
    
    def push(self, N):     
        if self.is_added(N) == "Y":
            return f"{N} is already in Set"
        self.items.append(N)
        
    def delete(self, N):
        if self.is_added(N) == 'Y':
            self.items.remove(N)
        

@timer
@memory_counter
def main():
    set = Set()
    results = []

    with open(INPUT_FILE) as f:
        M = int(f.readline())
        if not 1 <= M <= 10**6:
            raise ValueError("Неверные входные данные")

        commands = [command.strip() for command in f.readlines()]
        if len(commands) != M:
            raise ValueError("Неверные входные данные")

    for command in commands:
        N = int(command[1:].strip())
            
        if not abs(N) <= 10**9:
            raise ValueError("Неверные входные данные")
        
        if command[0] == "A":
            set.push(N)

        elif command[0] == "D":
            set.delete(N)

        elif command[0] == "?":
            N = int(command[1:].strip())
            results.append(set.is_added(N))

        else:
            print("Неизвестная операция")

    with open(OUTPUT_FILE, 'w') as f:
        for result in results:
            f.write(f"{result}\n")


if __name__ == "__main__":
    main()