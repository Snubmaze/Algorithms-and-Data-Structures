import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[3]))

from sem_1.utils.decorators import timer, memory_counter
import os

from bisect import bisect_left, bisect_right
from sortedcontainers import SortedList

PATH = os.path.dirname(__file__)
INPUT_FILE = f"{PATH}/input.txt"
OUTPUT_FILE = f"{PATH}/output.txt"

MOD = 1_000_000_001


@timer
@memory_counter
def main():
    with open(INPUT_FILE) as f:
        n = int(f.readline())
        s = SortedList()
        prefix = []
        x = 0
        result = []

        def add(val):
            if val in s:
                return
            i = s.bisect_left(val)
            s.add(val)
            if not prefix:
                prefix.append(val)
            elif i == 0:
                prefix.insert(0, val + prefix[0])
            elif i == len(prefix):
                prefix.append(prefix[-1] + val)
            else:
                prefix.insert(i, prefix[i - 1] + val)
                for j in range(i + 1, len(prefix)):
                    prefix[j] += val

        def delete(val):
            i = s.bisect_left(val)
            if i < len(s) and s[i] == val:
                s.remove(val)
                diff = val
                prefix.pop(i)
                for j in range(i, len(prefix)):
                    prefix[j] -= diff

        def find(val):
            return val in s

        def range_sum(l, r):
            left = s.bisect_left(l)
            right = s.bisect_right(r)
            if left >= right:
                return 0
            if left == 0:
                return prefix[right - 1]
            return prefix[right - 1] - prefix[left - 1]

        for _ in range(n):
            parts = f.readline().split()
            if not parts:
                continue

            op = parts[0]
            if op == '+':
                i = (int(parts[1]) + x) % MOD
                add(i)
            elif op == '-':
                i = (int(parts[1]) + x) % MOD
                delete(i)
            elif op == '?':
                i = (int(parts[1]) + x) % MOD
                result.append("Found" if find(i) else "Not found")
            elif op == 's':
                l = (int(parts[1]) + x) % MOD
                r = (int(parts[2]) + x) % MOD
                if l > r:
                    l, r = r, l
                x = range_sum(l, r)
                result.append(str(x))

    with open(OUTPUT_FILE, 'w') as f:
        f.write('\n'.join(result))


if __name__ == "__main__":
    main()
