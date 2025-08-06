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
        if not (2 <= n <= 10**3 and 1 <= m <= 10**3):
            raise ValueError("Неверные входные данные")

        graph = [[] for _ in range(n + 1)]

        for _ in range(m):
            a, b = map(int, f.readline().split())
            graph[a].append(b)
            graph[b].append(a)

        u, v = map(int, f.readline().split())
        if not (1 <= u <= n and 1 <= v <= n and u != v):
            raise ValueError("Неверные вершины u и v")

    visited = [False] * (n + 1)

    def dfs(node):
        if visited[node]:
            return
        visited[node] = True
        for neighbor in graph[node]:
            dfs(neighbor)

    dfs(u)

    with open(OUTPUT_FILE, 'w') as f:
        f.write("1\n" if visited[v] else "0\n")


if __name__ == "__main__":
    main()
