n , k = map(int, input().split())
h = list(map(int, input().split()))
h.sort(reverse = True)

for i in range(n):
    if h[i] < k:
        print(i)
        break
else:
    print(n)

