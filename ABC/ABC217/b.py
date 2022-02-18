import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

c = ["ABC", "ARC", "AGC", "AHC"]

s = []
for i in range(3):
    s.append(input().strip())

for ci in c:
    if ci not in s:
        print(ci)
        break
