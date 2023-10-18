# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
s = list(input())
q = int(input())

others = set()
is_all_learge = -1


def is_small(c):
    c = ord(c)

    return ord("a") <= c <= ord("z")


for i in range(n):
    if is_small(s[i]):
        others.add(i)


for i in range(q):
    t, x, c = map(str, input().split())
    x = int(x)-1

    if t == "1":
        if is_all_learge == 1 and is_small(c):
            others.add(x)
        elif is_all_learge == 0 and not is_small(c):
            others.add(x)
        s[x] = c

    elif t == "2":
        others.clear()
        is_all_learge = 0
    elif t == "3":
        others.clear()
        is_all_learge = 1

ans = []
if is_all_learge == 1:
    for i in range(n):
        if i in others:
            ans.append(s[i].lower())
        else:
            ans.append(s[i].upper())
elif is_all_learge == 0:
    for i in range(n):
        if i in others:
            ans.append(s[i].upper())
        else:
            ans.append(s[i].lower())
else:
    for i in range(n):
        ans.append(s[i])

print("".join(ans))
