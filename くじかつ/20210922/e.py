import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

x = input().strip()
m = int(input())

l = 0
for i in x:
    l = max(l, int(i))

ll = l+1
r = 10**18
n = len(x)
if n > 1:

    while l + 1 < r:
        mid = (l+r)//2
        tmp = 0
        for i in range(n):
            tmp += pow(mid, n-i-1)*int(x[i])
            if tmp > m:
                break
        if tmp <= m:
            l = mid
        else:
            r = mid

    print(l-ll+1)

else:
    if int(x) <= m:
        print(1)
    else:
        print(0)
