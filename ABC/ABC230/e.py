import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

d = []
for i in range(1, int(n**0.5)+1):
    if n % i == 0:
        d.append(i)
        if n % (n//i) == 0:
            d.append(n//i)

d.append(0)
d = list(set(d))
d.sort(reverse=True)

ans = 0
for i in range(len(d)-1):
    ans += (d[i]-d[i+1])*(n//d[i])
    print(ans, d[i], d[i+1])

print(ans)
