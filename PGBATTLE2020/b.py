import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# n = 10**5
# a = [100]*n
# b = [100]*n

a_sum = sum(a)
b_sum = sum(b)

if a_sum > b_sum:
    print("A")
elif a_sum < b_sum:
    print("B")
else:
    print("same")
