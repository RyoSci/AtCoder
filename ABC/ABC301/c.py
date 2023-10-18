# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from collections import defaultdict
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

s = list(input())
t = list(input())

n = len(s)
atcoder = set("atcoder")

ds = defaultdict(int)
dt = defaultdict(int)

for i in range(n):
    ds[s[i]] += 1
    dt[t[i]] += 1

a = 0
b = 0
st = set()
for key, val1 in ds.items():
    st.add(key)
    if key == "@":
        continue
    val2 = dt[key]

    if val1 == val2:
        continue
    elif key not in atcoder:
        print("No")
        exit()
    elif val1 > val2:
        b += val1-val2
    elif val1 < val2:
        a += val2-val1

for key, val1 in dt.items():
    if key in st:
        continue
    if key == "@":
        continue
    val2 = ds[key]

    if val1 == val2:
        continue
    elif key not in atcoder:
        print("No")
        exit()
    elif val1 > val2:
        a += val1-val2
    elif val1 < val2:
        b += val2-val1

if a <= ds["@"] and b <= dt["@"]:
    print("Yes")
else:
    print("No")
