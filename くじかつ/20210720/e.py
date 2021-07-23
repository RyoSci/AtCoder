n = int(input())
x = input()
# n = 2*10**5
# x = "1"*n

bit = 0
for i in x:
    if i == "1":
        bit += 1

a = bit+1
b = bit-1
flag = False
if b == 0:
    flag = True
b = max(b, 1)

a_sum = 0
b_sum = 0

for i in range(n):
    if x[i] == "1":
        a_sum = a_sum+pow(2, n-i-1, a)
        a_sum %= a
        b_sum = b_sum+pow(2, n-i-1, b)
        b_sum %= b


def popcount(x):
    tmp = 0
    while x > 0:
        if x % 2 == 1:
            tmp += 1
        x //= 2
    return tmp


for i in range(n):
    if x[i] == "0":
        m = a_sum+pow(2, n-i-1, a)
        m %= a
    else:
        if flag:
            print(0)
            continue
        m = b_sum-pow(2, n-i-1, b)
        m %= b
    cnt = 1
    while m != 0:
        cnt += 1
        m = m % popcount(m)

    print(cnt)
