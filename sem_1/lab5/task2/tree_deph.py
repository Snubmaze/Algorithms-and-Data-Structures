import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[3]))

import os
from sem_1.utils.decorators import timer, memory_counter
from sem_1.lab4.task1.stack import Stack


PATH = os.path.dirname(__file__)
INPUT_FILE = f"{PATH}/input.txt"
OUTPUT_FILE = f"{PATH}/output.txt"


def build_tree(n, parents):
    tree = [[] for _ in range(n)]
    root = -1
    for child_index, parent_index in enumerate(parents):
        if parent_index == -1:
            root = child_index
        else:
            tree[parent_index].append(child_index)
    return root, tree


def get_height(tree, node):
    if not tree[node]:
        return 1
    return 1 + max(get_height(tree, child) for child in tree[node])
        

@timer
@memory_counter
def main():
    with open(INPUT_FILE) as f:
        n = int(f.readline())
        if not (1 <= n <= 10**5):
            raise ValueError("Неверные входные данные")

        parents = list(map(int, f.readline().split()))
        if len(parents) != n:
            raise ValueError("Неверные входные данные")

    root, tree = build_tree(n, parents)
    height = get_height(tree, root)

    with open(OUTPUT_FILE, 'w') as f:
        f.write(str(height))


if __name__ == "__main__":
    main()
