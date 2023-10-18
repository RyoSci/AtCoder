# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, tt = map(str, input().split())
tt = list(tt)
n = int(n)


ans = []
for _ in range(n):
    s = input()
    s = list(s)

    flag = True
    i = 0
    j = 0
    cnt = 0

    if len(s) == len(tt):
        while i < len(s):
            if s[i] == tt[j]:
                i += 1
                j += 1
            else:
                i += 1
                j += 1
                if cnt > 0:
                    flag = False
                    break
                cnt += 1

    elif len(s) == len(tt) - 1:
        while i < len(s):
            if s[i] == tt[j]:
                i += 1
                j += 1
            else:
                j += 1
                if cnt > 0:
                    flag = False
                    break
                cnt += 1

    elif len(s) - 1 == len(tt):
        while i < len(tt):
            if s[j] == tt[i]:
                i += 1
                j += 1
            else:
                j += 1
                if cnt > 0:
                    flag = False
                    break
                cnt += 1

    else:
        flag = False

    if flag:
        ans.append(_+1)

print(len(ans))
print(*ans)
