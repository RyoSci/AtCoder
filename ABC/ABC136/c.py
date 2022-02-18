n = int(input())

h = list(map(int, input().split()))
h[0] -= 1
for i in range(1, n):
    if h[i - 1] < h[i]:
        h[i] -= 1
    elif h[i - 1] == h[i]:
        pass
    else:
        print("No")
        break
else:
    print("Yes")