n, k = map(int, input().split())
a = list(map(int, input().split()))

if (n + k - 1) // k == 1:
    print(1)
else:
    res = ((n - k) + (k - 2)) // (k - 1) + 1
    print(res)
