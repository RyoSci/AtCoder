n, k, q = map(int, input().split())
an = [0] * n
for i in range(q):
    answer = int(input())
    an[answer - 1] += 1

for i in range(n):
    if an[i] + k > q:
        print("Yes")
    else:
        print("No")
