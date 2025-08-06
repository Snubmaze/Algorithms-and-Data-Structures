import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[3]))

from sem_1.utils.decorators import timer, memory_counter
from sem_1.lab1.task1.insertion import insertion_sort
import os
import random


PATH = os.path.dirname(__file__)
INPUT_FILE = f"{PATH}/input.txt"
OUTPUT_FILE = f"{PATH}/output.txt"


def count_segments_covering_points(segments, points):
    events = []

    for a, b in segments:
        if a > b:
            a, b = b, a
        events.append((a, 'L'))
        events.append((b, 'R'))

    for idx, x in enumerate(points):
        events.append((x, 'P', idx))

    events.sort(key=lambda e: (e[0], 0 if e[1] == 'L' else 1 if e[1] == 'P' else 2))

    result = [0] * len(points)
    active_segments = 0

    for event in events:
        if event[1] == 'L':
            active_segments += 1
        elif event[1] == 'R':
            active_segments -= 1
        else:
            _, _, idx = event
            result[idx] = active_segments

    return result


def main():
    with open(INPUT_FILE, "r") as f:
        s, p = map(int, f.readline().split())
        segments = [tuple(map(int, f.readline().split())) for _ in range(s)]
        points = list(map(int, f.readline().split()))

    result = count_segments_covering_points(segments, points)

    with open(OUTPUT_FILE, "w") as f:
        f.write(' '.join(map(str, result)))


if __name__ == "__main__":
    main()
