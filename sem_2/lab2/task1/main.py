import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[3]))

from sem_1.utils.decorators import timer, memory_counter
import os


PATH = os.path.dirname(__file__)
INPUT_FILE = f"{PATH}/input.txt"
OUTPUT_FILE = f"{PATH}/output.txt"


def in_order(tree) -> list[int]:
    result = []

    def dfs(i):
        if i == -1:
            return
        key, left, right = tree[i]
        dfs(left)
        result.append(key)
        dfs(right)

    dfs(0)  # корень — всегда 0
    return result


def pre_order(tree) -> list[int]:
    result = []

    def dfs(i):
        if i == -1:
            return
        key, left, right = tree[i]
        result.append(key)
        dfs(left)
        dfs(right)

    dfs(0)
    return result


def post_order(tree) -> list[int]:
    result = []

    def dfs(i):
        if i == -1:
            return
        key, left, right = tree[i]
        dfs(left)
        dfs(right)
        result.append(key)

    dfs(0)
    return result



@timer
@memory_counter
def main():
    with open(INPUT_FILE) as f:
        n = int(f.readline())
        if not (1 <= n <= 10**5):
            raise ValueError("Неверные входные данные")
        
        nodes = []
        for _ in range(n):
            node = list(map(int, f.readline().split()))
            
            K = node[0]
            if not 0 <= K <= 10**9:
                raise ValueError("Неверные входные данные")
            
            L, R = node[1], node[2]
            if not (-1 <= L <= n - 1 or -1 <= R <= n - 1) or (L != -1 and R != -1 and L == R):
                raise ValueError("Неверные входные данные")

            nodes.append((K, L, R))  # сохраняем как кортеж

    in_order_result = in_order(nodes)
    pre_order_result = pre_order(nodes)
    post_order_result = post_order(nodes)

    with open(OUTPUT_FILE, 'w') as f:
        f.write(' '.join(map(str, in_order_result)) + '\n')
        f.write(' '.join(map(str, pre_order_result)) + '\n')
        f.write(' '.join(map(str, post_order_result)) + '\n')



if __name__ == "__main__":
    main()