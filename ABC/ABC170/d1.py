n = int(input())
# a = list(map(int, input().split()))
a = list(range(1, n))
a.sort()
factor = []
set_factor = set()
counter = 0
if n != 1:
    if a[0] != a[1]:
        counter += 1

    set_factor.add(a[0])
    factor.append(a[0])

    for i in range(1, n - 1):
        back = a[i - 1]
        forward = a[i + 1]
        if a[i] not in set_factor:
            for j in factor:
                if a[i] % j == 0:
                    break
            else:
                if a[i] != forward and a[i] != back:
                    counter += 1
                set_factor.add(a[i])
                factor.append(a[i])
            
    if a[n - 1] != a[n - 2] :
        for i in factor:
            if a[n - 1] % i == 0:
                break
        else:
            counter += 1
    print(counter)
else:
    print(1)