import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

# n = 10**5
# a = []
# for i in range(1, n+1):
#     a.append(i)
#     a.append(i)

pair = [-1]*n

for i in range(2*n):
    if pair[a[i]-1] == -1:
        pair[a[i]-1] = i
    else:
        pair[a[i]-1] = i-pair[a[i]-1]-1

ks = [0]*(2*n-1)
for i in range(n):
    ks[pair[i]] += 1

for i in range(1, 2*n-1):
    ks[i] += ks[i-1]

print(*ks, sep="\n")
