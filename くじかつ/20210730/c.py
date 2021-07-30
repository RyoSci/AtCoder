n = int(input())
a = [int(input()) for _ in range(5)]

res = 5+(n+min(a)-1)//min(a)-1

print(res)
