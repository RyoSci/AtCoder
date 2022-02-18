import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

s = input().strip()
k = int(input().strip())
# s = "c"*5000
# k = 5

n = len(s)
total = set()
for i in range(n):
    for j in range(1, k+1):
        total.add("".join(s[i:i+j]))

total = list(total)
total.sort()
print(total[k-1])
# print(total)
