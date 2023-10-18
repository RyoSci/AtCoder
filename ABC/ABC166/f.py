# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18
n, *abc = map(int, input().split())

s = []
for i in range(n):
    si = input()
    s.append(si)

ans = []
for i in range(n):
    s0 = ord(s[i][0]) - ord("A")
    s1 = ord(s[i][1]) - ord("A")

    if abc[s0] == 0 and abc[s1] == 0:
        print("No")
        exit()
    elif abc[s0] == 1 and abc[s1] == 1:
        # 次を見る
        if i == n-1 or (i != n-1 and s[i] == s[i+1]):
            abc[s0] -= 1
            abc[s1] += 1
            ans.append("ABC"[s1])
        else:
            ss0 = set(s[i])
            ss1 = set(s[i+1])

            ms = ss0 - ss1
            ps = ss0 & ss1
            ms = next(iter(ms))
            ps = next(iter(ps))

            ms = ord(ms) - ord("A")
            ps = ord(ps) - ord("A")

            abc[ps] += 1
            abc[ms] -= 1
            ans.append("ABC"[ps])
    else:
        if abc[s0] > abc[s1]:
            abc[s0] -= 1
            abc[s1] += 1
            ans.append("ABC"[s1])
        else:
            abc[s0] += 1
            abc[s1] -= 1
            ans.append("ABC"[s0])

print("Yes")
print(*ans, sep="\n")
