import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

x = int(input())

if x % 3 == 0:
    print("Bob")
else:
    print("Sakky")
