from itertools import permutations
n = int(input())

xy = [list(map(int, input().split())) for _ in range(n)]

total = 0
div = 0
for i in permutations(range(n)):
    div += 1
    for j in range(n-1):
        total += ((xy[i[j]][0]-xy[i[j+1]][0])**2 +
                  (xy[i[j]][1]-xy[i[j+1]][1])**2)**0.5

print(total/div)
