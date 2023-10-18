# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, k = map(int, input().split())
a = list(map(int, input().split()))

tot = sum(a)

div = set()
for i in range(1, tot):
    if i*i > tot:
        break
    if tot % i == 0:
        div.add(i)
        div.add(tot//i)


div = list(div)
ans = 1
for divi in div:
    a_hat = []
    for i in range(n):
        a_hat.append(a[i] % divi)
    a_hat.sort()
    res = 0
    j = n-1
    for i in range(n):
        while a_hat[i] != 0:
            tmp = min(divi-a_hat[j], a_hat[i])

            a_hat[j] += tmp
            a_hat[j] %= divi
            a_hat[i] -= tmp
            res += tmp
            if a_hat[j] == 0:
                j -= 1

    if res <= k:
        ans = max(ans, divi)

print(ans)
