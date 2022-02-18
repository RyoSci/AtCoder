import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
x = int(input())

a_sum = sum(a)

res = n*(x//a_sum)
mod = x % a_sum

for i in range(n):
    mod -= a[i]
    res += 1
    if mod < 0:
        break

print(res)
