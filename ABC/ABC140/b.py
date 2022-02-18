n = int(input())
an = list(map(int, input().split()))
bn = list(map(int, input().split()))
cn = list(map(int, input().split()))

satisfy = 0
for i in range(n):
    satisfy += bn[an[i] - 1]

for i in range(n - 1):
    if an[i] + 1 == an[i + 1]:
        satisfy += cn[an[i] - 1]

print(satisfy)