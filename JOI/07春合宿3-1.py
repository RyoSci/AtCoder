# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

s = input()
s = [ord(i) - ord("A") for i in s]
n = len(s)

f = [1]*30
for i in range(1, 30):
    f[i] *= f[i-1] * i

ans = 0
for i in range(n):
    # siが自分より右で小さい数
    st = set()
    for j in range(i+1, n):
        if s[i] > s[j]:
            st.add(s[j])

    # 分布
    tmp = [0]*26
    for j in range(i, n):
        tmp[s[j]] += 1

    # sよりも先に登場した文字列の数
    for j in st:
        tmp[j] -= 1

        cnt = f[n-1-i]
        for k in range(26):
            cnt //= f[tmp[k]]
        ans += cnt

        tmp[j] += 1

ans += 1
print(ans)
