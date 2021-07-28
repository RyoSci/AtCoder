a, b = map(int, input().split())

dis = b-a
for i in range(dis, 0, -1):
    if (a+i-1)//i != b//i:
        ans = i
        break

print(ans)
