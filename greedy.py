from collections import Counter
from functools import reduce


def anagram(line):
    len_line = len(line)
    ct = Counter(line)

    def fn(idx):
        if idx == len_line:
            return 0

        ret = 0

        for key, val in ct.items():
            if val == 0:
                continue

            if key < line[idx]:
                ct[key] -= 1
                curr = reduce(lambda x, y: x * y, range(1, len_line - idx))
                for val in ct.values():
                    if val >= 2:
                        curr //= reduce(lambda x, y: x * y, range(2, val + 1))
                ret += curr
                ct[key] += 1

            elif key == line[idx]:
                ct[key] -= 1
                ret += fn(idx + 1)
                ct[key] += 1

        return ret

    return fn(0) + 1


# with open("anagram.in") as f:
#     line = f.readline().strip()
line = input().strip()
print(anagram(line))


# print(anagram("EARTH"))
# print(anagram("HEART"))
# print(anagram("IOI"))
