import itertools

n = int(input())
d = list(map(int, input().split()))

recovery = 0
for i in itertools.combinations(range(n), 2):
    recovery += d[i[0]] * d[i[1]]
print(recovery)