from itertools import permutations
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

# s0 = input().rstrip()
# s1 = input().rstrip()
# s2 = input().rstrip()
s0 = sys.argv[1]
s1 = sys.argv[2]
s2 = sys.argv[3]

start = set()
start.add(s0[0])
start.add(s1[0])
start.add(s2[0])

d = dict()

for i in s0+s1+s2:
    if i not in d:
        d[i] = 0

if len(d) > 10:
    print("UNSOLVABLE")
else:
    keys = list(d.keys())
    l = max([len(si) for si in [s0, s1, s2]])
    s0 = s0.zfill(l)[::-1]
    s1 = s1.zfill(l)[::-1]
    s2 = s2.zfill(l)[::-1]
    for p in permutations(range(10), len(d)):
        flag = False
        for i, key in enumerate(keys):
            if p[i] == 0 and key in start:
                flag = True
                break
            d[key] = p[i]
        d["0"] = 0
        if flag:
            continue
        pre = 0
        for i in range(l):
            now = d[s0[i]]+d[s1[i]]
            now %= 10
            if now+pre != d[s2[i]]:
                break
            pre = d[s0[i]]+d[s1[i]]
            pre //= 10
        else:
            s0 = int("".join(list((map(lambda x: str(d[x]), s0[::-1])))))
            s1 = int("".join(list((map(lambda x: str(d[x]), s1[::-1])))))
            s2 = int("".join(list((map(lambda x: str(d[x]), s2[::-1])))))
            print(s0)
            print(s1)
            print(s2)
            exit()
    else:
        print("UNSOLVABLE")
