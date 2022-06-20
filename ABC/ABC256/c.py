# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18
hw = list(map(int, input().split()))
h = hw[:3]
w = hw[3:]

ans = 0
g = [[0]*3 for _ in range(3)]
for i in range(1, h[0]-1):
    for j in range(1, h[0]-1):
        k = h[0]-i-j
        if k <= 0:
            break
        # g[0][0] = i
        # g[0][1] = j
        # g[0][2] = k
        for ii in range(1, h[1]-1):
            for jj in range(1, h[1]-1):
                kk = h[1]-ii-jj
                if kk <= 0:
                    break
                # g[1][0] = ii
                # g[1][1] = jj
                # g[1][2] = kk
                for iii in range(1, h[2]-1):
                    for jjj in range(1, h[2]-1):
                        kkk = h[2]-iii-jjj
                        if kkk <= 0:
                            break
                        # g[2][0] = iii
                        # g[2][1] = jjj
                        # g[2][2] = kkk
                        # flag = True
                        # for jjjj in range(3):
                        #     tmp = 0
                        #     for iiii in range(3):
                        #         tmp += g[iiii][jjjj]
                        #     if tmp != w[jjjj]:
                        #         flag = False
                        #         break
                        # if flag:
                        #     ans += 1
                        if w[0] == i+ii+iii and w[1] == j+jj+jjj and w[2] == k+kk+kkk:
                            ans += 1

print(ans)
