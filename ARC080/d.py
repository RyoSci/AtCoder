h, w = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))

hi, wi = 0, 0
out = [["" for i in range(w)] for i in range(h)]

for i in range(n):
    while a[i] != 0:
        out[hi][wi] = i + 1
        if hi % 2 == 0:
            wi += 1
            if wi == w:
                hi += 1
                wi -= 1
        else:
            wi -= 1
            if wi == -1:
                hi += 1
                wi += 1
        a[i] -= 1

for hi in range(h):
    print(*out[hi])
