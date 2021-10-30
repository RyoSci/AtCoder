import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, q = map(int, input().split())
l = []
for i in range(n):
    l.append([i, i])


ans = []
for i in range(q):
    querry = list(map(int, input().split()))
    if querry[0] == 1:
        x, y = querry[1], querry[2]
        x -= 1
        y -= 1
        l[x][1] = y
        l[y][0] = x
    elif querry[0] == 2:
        x, y = querry[1], querry[2]
        x -= 1
        y -= 1
        l[x][1] = x
        l[y][0] = y
    else:
        x = querry[1]
        x -= 1
        res = []
        res.append(x+1)
        ll = x
        while 1:
            if ll == l[ll][0]:
                break
            else:
                ll = l[ll][0]
                res.append(ll+1)
        rr = x
        res = res[::-1]
        while 1:
            if rr == l[rr][1]:
                break
            else:
                rr = l[rr][1]
                res.append(rr+1)
        ans.append([len(res), res])

for i in range(len(ans)):
    print(ans[i][0], *ans[i][1])
