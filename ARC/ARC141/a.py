# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

t = int(input())
for i in range(t):
    c_ = input()
    n_ = len(c_)
    ans = 0
    for j in range(2, 20):
        if n_ % j == 0:
            c = c_
            n = n_
        else:
            c = "9"*(n_-1)
            n = n_-1
        if n < j:
            continue
        tmp = []
        dj = n//j
        for k in range(0, n, dj):
            tmp.append(c[k:k+dj])
        # print(tmp)
        l = tmp[0]
        flag = True
        is_up = False
        for k in tmp[1:]:
            if int(l) == int(k):
                continue
            elif int(l) > int(k):
                if not is_up:
                    flag = False
                    break
            else:
                is_up = True
        if flag:
            ans = max(ans, int(l*j))
        else:
            ans = max(ans, int(str(int(l)-1)*j))

    print(ans)
