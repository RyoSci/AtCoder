n, k = map(int, input().split())
one_and_dis = []
for i in range(n):
    a, b = map(int, input().split())
    one_and_dis.append(b)
    one_and_dis.append(a-b)

one_and_dis.sort(reverse=True)
print(sum(one_and_dis[:k]))
