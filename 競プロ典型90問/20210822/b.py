from bisect import bisect_left

n = int(input())
a = list(map(int, input().split()))
a = [-10**18] + a + [10**18]
a.sort()
q = int(input())
ans = []
for i in range(q):
    b = int(input())
    index = bisect_left(a, b)
    res = min(abs(a[index-1]-b), abs(a[index]-b))
    ans.append(res)

print(*ans, sep="\n")
