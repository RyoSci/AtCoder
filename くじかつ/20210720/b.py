n, k, q = map(int, input().split())
a = [k]*n

for i in range(q):
    ai = int(input())
    a[ai-1] += 1

for i in range(n):
    if a[i]-q > 0:
        print("Yes")
    else:
        print("No")
