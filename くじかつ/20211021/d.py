import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))

pos = [0]*n
for i in range(n):
    pos[p[i]-1] = i

ans = []
bridges = [1]*(n-1)
for i in range(n):
    while pos[i] != i:
        if pos[i] > i and bridges[pos[i]-1] == 1:
            bridges[pos[i]-1] = 0
            pos[i] -= 1
            pos[p[pos[i]]-1] += 1
            p[pos[i]], p[pos[i]+1] = p[pos[i]+1], p[pos[i]]
            ans.append(pos[i]+1)
        else:
            print(-1)
            exit()

    flag1 = False
    flag2 = False
    if i-1 > 0:
        if bridges[i-1] == 0:
            flag1 = True
    else:
        flag1 = True
    if i < n-1:
        if bridges[i] == 0:
            flag2 = True
    else:
        flag2 = True
    if flag1 and flag2:
        continue
    else:
        print(-1)
        exit()
else:
    print(*ans, sep="\n")
