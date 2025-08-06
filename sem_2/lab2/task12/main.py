import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[3]))

from sem_1.utils.decorators import timer, memory_counter
import os

PATH = os.path.dirname(__file__)
INPUT_FILE = f"{PATH}/input.txt"
OUTPUT_FILE = f"{PATH}/output.txt"


class Node:
    def __init__(self, key, left_index, right_index):
        self.key = key
        self.left_index = left_index
        self.right_index = right_index
        self.height = 0
        self.balance = 0


def compute_heights_and_balances(nodes, index):
    if index == 0:
        return 0

    node = nodes[index]
    left_h = compute_heights_and_balances(nodes, node.left_index)
    right_h = compute_heights_and_balances(nodes, node.right_index)

    node.height = 1 + max(left_h, right_h)
    node.balance = right_h - left_h

    return node.height


@timer
@memory_counter
def main():
    with open(INPUT_FILE) as f:
        n = int(f.readline())
        if not (0 <= n <= 2 * 10**5):
            raise ValueError("Неверное количество вершин")

        nodes = [None] * (n + 1)

        for i in range(1, n + 1):
            parts = f.readline().split()
            if len(parts) != 3:
                raise ValueError("Неверный формат строки узла")

            k, l, r = map(int, parts)
            nodes[i] = Node(k, l, r)

    if n > 0:
        compute_heights_and_balances(nodes, 1)

    with open(OUTPUT_FILE, 'w') as f:
        for i in range(1, n + 1):
            f.write(f"{nodes[i].balance}\n")


if __name__ == "__main__":
    main()
