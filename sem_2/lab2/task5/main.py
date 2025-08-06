import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[3]))

from sem_1.utils.decorators import timer, memory_counter
import os


PATH = os.path.dirname(__file__)
INPUT_FILE = f"{PATH}/input.txt"
OUTPUT_FILE = f"{PATH}/output.txt"


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node

    def exists(self, key):
        return self._exists(self.root, key)

    def _exists(self, node, key):
        if node is None:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self._exists(node.left, key)
        else:
            return self._exists(node.right, key)

    def next(self, key):
        return self._next(self.root, key)

    def _next(self, node, key):
        result = None
        while node:
            if node.key > key:
                result = node
                node = node.left
            else:
                node = node.right
        return result.key if result else "none"

    def prev(self, key):
        return self._prev(self.root, key)

    def _prev(self, node, key):
        result = None
        while node:
            if node.key < key:
                result = node
                node = node.right
            else:
                node = node.left
        return result.key if result else "none"

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # min node in right subtree
            min_larger_node = self._find_min(node.right)
            node.key = min_larger_node.key
            node.right = self._delete(node.right, min_larger_node.key)
        return node

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node


@timer
@memory_counter
def main():
    tree = BST()
    result = []

    with open(INPUT_FILE) as f:
        for line in f:
            parts = line.strip().split()
            if not parts:
                continue

            cmd = parts[0]
            if len(parts) == 2:
                x = int(parts[1])
                if cmd == "insert":
                    tree.insert(x)
                elif cmd == "delete":
                    tree.delete(x)
                elif cmd == "exists":
                    result.append("true" if tree.exists(x) else "false")
                elif cmd == "next":
                    res = tree.next(x)
                    result.append(str(res))
                elif cmd == "prev":
                    res = tree.prev(x)
                    result.append(str(res))
                else:
                    raise ValueError(f"Неизвестная команда: {cmd}")
            else:
                raise ValueError("Неверный формат команды")

    with open(OUTPUT_FILE, 'w') as f:
        f.write('\n'.join(result))


if __name__ == "__main__":
    main()
