n = int(input())
zero = [0] * (n+1)
one = [0] * (n+1)
zero[0] = 1

for i in range(1, n+1):
    zero[i] = one[i-1]
    one[i] = zero[i-1] + one[i-1]

print(zero[n] + one[n])
