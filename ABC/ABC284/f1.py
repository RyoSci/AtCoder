
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

"https://qiita.com/Pro_ktmr/items/16904c9570aa0953bf05"


def z_alog(s: str):
    z = [0]*len(s)
    z[0] = len(s)
    i = 1
    j = 0
    while i < len(s):
        while i + j < len(s) and s[j] == s[i + j]:
            j += 1
        z[i] = j

        if j == 0:
            i += 1
            continue

        k = 1
        while k < j and k + z[k] < j:
            z[i + k] = z[k]
            k += 1
        i += k
        j -= k
    return z


n = int(input())
t = input()
t0 = t[:n] + t[n:][::-1]
z0 = z_alog(t0)+[0]
t1 = t[n:][::-1]+t[:n]
z1 = z_alog(t1)+[0]
# print(z0)
# print(z1)

for i in range(0, n+1):
    # print(f"{i}\t {t0[:i]}\t {t0[2*n-i:]}\t {t1[:n-i]}\t {t1[n+i:]}")
    # print(z0[2*n-i], z1[n+i])
    if z0[2*n-i] == i and z1[n+i] == n-i:
        print(t[:i]+t[n+i:])
        print(i)
        exit()

print(-1)
