n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_num = 0
b_num = 0
book_num = 0
passed_k = 0
for i in range(n):
    if a[i] + passed_k <= k:
        a_num += 1
        passed_k += a[i]
    else:
        break
for i in range(m):
    if b[i] + passed_k <= k:
        b_num += 1
        passed_k += b[i]
    else:
        break
book_num = a_num + b_num

while a_num > 0:
    passed_k -= a[a_num - 1]
    a_num -= 1
    while b_num < m:
        if passed_k + b[b_num] <= k:
            passed_k += b[b_num]
            b_num += 1
        else:
            break
    book_num = max(book_num, a_num + b_num)
    if b_num == m:
        break

print(book_num)