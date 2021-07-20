from bisect import bisect_left
n, m = map(int, input().split())
h = sorted(list(map(int, input().split())))
w = sorted(list(map(int, input().split())))

even = [0]
for i in range(1, n, 2):
    even.append(abs(h[i]-h[i+1]))
odd = [0]
for i in range(0, n-1, 2):
    odd.append(abs(h[i]-h[i+1]))

tmp = sum(even)
res = 10**18
for i in range(0, n, 2):
    tmp = tmp+odd[i//2]-even[i//2]
    index = bisect_left(w, h[i])
    index = min(index, m-1)
    res = min(res, tmp+abs(h[i]-w[index]), tmp+abs(h[i]-w[index-1]))

print(res)
