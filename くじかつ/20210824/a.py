n = int(input())
a = list(map(int, input().split()))
b = [[a[i], i] for i in range(n)]
b.sort()
print(b[-2][1]+1)
