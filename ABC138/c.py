n = int(input())
v = list(map(int, input().split()))
v.sort()

value = v[0] 
for i in range(1, n):
    value = (value + v[i]) / 2 
print(value)
