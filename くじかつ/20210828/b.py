import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))

# points = 1
# for i in range(k):
#     points *= a[i]

for i in range(k, n):
    # now = points*a[i]//a[i-k]
    # if points < now:
    #     print("Yes")
    # else:
    #     print("No")
    if a[i-k] < a[i]:
        print("Yes")
    else:
        print("No")
