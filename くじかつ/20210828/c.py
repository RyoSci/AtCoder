import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

if sum(a) < sum(b):
    print(-1)
    exit()
else:
    cp = []
    cm = []
    for i in range(n):
        dis = a[i]-b[i]
        if dis >= 0:
            cp.append(dis)
        else:
            cm.append(dis)
    cp.sort(reverse=True)
    cnt = len(cm)
    cpi = 0
    for cmi in cm:
        while cmi < 0:
            if cp[cpi] == 0:
                cpi += 1
            dis = min(0, cmi+cp[cpi])
            cp[cpi] -= (dis-cmi)
            cmi = dis
    if cnt == 0:
        print(0)
    else:
        print(cnt+cpi+1)
