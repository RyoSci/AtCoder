n, q = map(int, input().split())
s = input()

ac_counter = [0] * n
counter = 0
for i in range(n - 1):
    # ac_counter[i] = counter
    if s[i:i+2] == "AC":
        counter += 1
    ac_counter[i + 1] = counter

for i in range(q):
    l, r = map(int, input().split())
    print(ac_counter[r - 1] - ac_counter[l - 1])
# print(ac_counter)