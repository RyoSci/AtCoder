a, v = map(int, input().split())
b, w = map(int, input().split())
t = int(input())

if v <= w:
    ans = "NO"
elif abs(b-a) > t*(v-w):
    ans = "NO"
else:
    ans = "YES"

print(ans)
