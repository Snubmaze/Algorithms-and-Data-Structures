import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[3]))

from sem_1.utils.decorators import timer, memory_counter
import os


PATH = os.path.dirname(__file__)
INPUT_FILE = f"{PATH}/input.txt"
OUTPUT_FILE = f"{PATH}/output.txt"


def hash_str(
            S: str, 
            x: int = 263, 
            p: int = 1000000007, 
            m: int = 5
        ):
    result = 0
    for i in range(len(S)):
        result += (ord(S[i]) * x**i) 
    result = result % p % m
    return result


class HashTable:
    def __init__(self, m):
        self.items = [[] for _ in range(m)]

    def add_string(self, string):
        idx = hash_str(string, m=len(self.items))
        if string not in self.items[idx]:
            self.items[idx].insert(0, string)
        
    
    def del_string(self, string):     
        idx = hash_str(string, m=len(self.items))
        for st in self.items[idx]:
            if st == string:
                self.items[idx].remove(st)
        
    def find_string(self, string):
        idx = hash_str(string, m=len(self.items))
        for st in self.items[idx]:
            if st == string:
                return "yes"
        return "no"
    
    def check_i(self, i):
        return " ".join(map(str, self.items[i])) if len(self.items[i]) else ""
        


@timer
@memory_counter
def main():
    results = []

    with open(INPUT_FILE) as f:
        m = int(f.readline())
        N = int(f.readline())
        if not (1 <= N <= 10**5) or not (N/5 <= m <= N):
            raise ValueError("Неверные входные данные")

        cmds = [line.strip() for line in f.readlines()]

        if len(cmds) != N or any(len(cmd) >= 15 for cmd in cmds):
            raise ValueError("Неверные входные данные")
        
    ht = HashTable(m)

    for cmd in cmds:
        key_word, string = cmd.split(' ')
        
        if key_word == "add":
            ht.add_string(string)

        elif key_word == "del":
            ht.del_string(string)

        elif key_word == "check":
            results.append(ht.check_i(int(string)))

        elif key_word == "find":
            results.append(ht.find_string(string))


    with open(OUTPUT_FILE, 'w') as f:
        for result in results:
            f.write(f"{result}\n")


if __name__ == "__main__":
    main()