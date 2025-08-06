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
        if not (2 <= n <= 300 and 1 <= m <= 10**5):
            raise ValueError("Неверные входные данные")

        dist = [[float('inf')] * n for _ in range(n)]
        adj = [[False] * n for _ in range(n)]

        for _ in range(m):
            u, v = map(int, f.readline().split())
            u -= 1
            v -= 1
            dist[u][v] = 0
            adj[u][v] = True

        for i in range(n):
            for j in range(n):
                if i != j and dist[i][j] == float('inf') and adj[j][i]:
                    dist[i][j] = 1

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        max_k = 0
        for i in range(n):
            for j in range(n):
                if i != j:
                    max_k = max(max_k, dist[i][j])

        with open(OUTPUT_FILE, "w") as f:
            f.write(str(int(max_k)) + "\n")


if __name__ == "__main__":
    main()
