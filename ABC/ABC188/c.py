n = int(input())
a_ = list(map(int, input().split()))
a = []
for i in range(2**n):
    a.append([a_[i], i])


ans = min(max(a[:2**(n-1)], key=lambda x: x[0]),
          max(a[2**(n-1):], key=lambda x: x[0]))
print(ans[1]+1)
