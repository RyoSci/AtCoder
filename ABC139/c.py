n = int(input())
h = list(map(int, input().split()))

max_jump = 0
tmp_jump = 0
for i in range(n - 1):
    if h[i] >= h[i + 1]:
        tmp_jump += 1
        max_jump = max(max_jump, tmp_jump)
    else:
        tmp_jump = 0

print(max_jump)