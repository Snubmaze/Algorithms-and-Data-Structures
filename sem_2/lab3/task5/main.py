import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[3]))

from sem_1.utils.decorators import timer, memory_counter
import os

PATH = os.path.dirname(__file__)
INPUT_FILE = f"{PATH}/input.txt"
OUTPUT_FILE = f"{PATH}/output.txt"


@timer
@memory_counter
def main():
    with open(INPUT_FILE) as f:
        n, m = map(int, f.readline().split())
        if not (1 <= n <= 10**4 and 0 <= m <= 10**4):
            raise ValueError("Неверные входные данные")

        graph = [[] for _ in range(n + 1)]
        reverse_graph = [[] for _ in range(n + 1)]

        for _ in range(m):
            u, v = map(int, f.readline().split())
            graph[u].append(v)
            reverse_graph[v].append(u)

    visited = [False] * (n + 1)
    order = []

    def dfs(v):
        visited[v] = True
        for to in graph[v]:
            if not visited[to]:
                dfs(to)
        order.append(v)

    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)

    visited = [False] * (n + 1)
    scc_count = 0

    def reverse_dfs(v):
        visited[v] = True
        for to in reverse_graph[v]:
            if not visited[to]:
                reverse_dfs(to)

    for v in reversed(order):
        if not visited[v]:
            reverse_dfs(v)
            scc_count += 1

    with open(OUTPUT_FILE, 'w') as f:
        f.write(str(scc_count) + '\n')


if __name__ == "__main__":
    main()
