import os


def read_ints(path: str) -> tuple[int, list[int]]:
    with open(f'{path}/input.txt', 'r') as f:
        n = int(f.readline())
        arr = [int(i) for i in f.readline().split(", ")]
    return n, arr


def write_output(path: str, data: list[int]) -> None:
    with open(f'{path}/output.txt', 'w') as f:
        f.write(' '.join(str(x) for x in data))
