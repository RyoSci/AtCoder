n = int(input())
a = list(map(int, input().split()))
# a = list(range(1, n))
a.sort()
set_factor = set()
counter = 0

if n != 1:
    if a[0] != a[1]:
        counter += 1
    set_factor.add(a[0])

    for i in range(1, n - 1):
        back = a[i - 1]
        if a[i] != back:
            forward = a[i + 1]
            if a[i] != forward:
                for j in range(1, int(a[i] ** (1/2)) + 1):
                    if a[i] % j == 0:
                        high_factor = a[i] // j
                        if j in set_factor:
                            break
                        elif high_factor in set_factor:
                            break
                else:
                    counter += 1
            set_factor.add(a[i])

    if a[n - 2] != a[n - 1]:
        for j in range(1, int(a[n - 1] ** (1/2)) + 1):
            if a[n - 1] % j == 0:
                high_factor = a[n - 1] // j
                if j in set_factor:
                    break
                elif  high_factor in set_factor:
                    break
        else:
            counter += 1
else:
    counter = 1
print(counter)
# print(set_factor)