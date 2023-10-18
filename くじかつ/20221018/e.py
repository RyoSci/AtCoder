# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m = map(int, input().split())
a = list(map(int, input().split()))

nums = [[-1] for _ in range(m+1)]

for i in range(n):
    if a[i] < 0:
        start = (-a[i]+i)//(i+1)
    else:
        start = 0

    now = a[i]+(i+1)*start

    while now < n:
        if start > m:
            break
        nums[start].append(now)
        start += 1
        now += (i+1)


ans = []
for i in range(1, m+1):
    nums[i].sort()
    for j in range(len(nums[i])-1):
        if nums[i][j]+1 < nums[i][j+1]:
            ans.append(nums[i][j]+1)
            break
    else:
        ans.append(nums[i][-1]+1)

# print(nums)
print(*ans)
