import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

abc = input().strip()
a, b, c = abc[0], abc[1], abc[2]

print(int(a+b+c)+int(b+c+a)+int(c+a+b))
