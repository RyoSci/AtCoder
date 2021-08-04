ab = [0]*4
for i in range(3):
    a, b = map(lambda x: int(x)-1, input().split())
    ab[a] += 1
    ab[b] += 1

ab.sort()
if ab == [1, 1, 2, 2]:
    print("YES")
else:
    print("NO")
