# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    if n == 1:
        print(*a)

    else:
        mxpos = 1

        for i in range(1, n):
            if a[mxpos] < a[i]:
                mxpos = i

        tot = []
        tmp = a[:mxpos+1][::-1]
        r = a[mxpos+1:]
        tot.append(tuple(r+tmp))

        for li in range(mxpos):
            l = a[:li]
            tmp = a[li:mxpos][::-1]
            r = a[mxpos:]
            tot.append(tuple(r+tmp+l))

        l = a[:mxpos]
        tmp = a[mxpos:mxpos+1][::-1]
        r = a[mxpos+1:]
        tot.append(tuple(r+tmp+l))

        tot.sort(reverse=True)
        # print(tot)
        print(*tot[0])
