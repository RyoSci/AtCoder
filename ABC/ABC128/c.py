n , m = map(int, input().split())

switch = []
for i in range(m):
    line = list(map(int, input().split()))
    k, s = line[0], line[1::]
    switch.append(s)

is_on_off = list(map(int, input().split()))

print("######################################")
res = 0
for i in range(1 << n):
    on_off_state = []
    for index in range(n):
        if i >> index & 1 == 1:
            on_off_state.append("on")
        else:
            on_off_state.append("off")
    for ki in range(m):
        on_off_counter = 0
        for i_switch in switch[ki]:
            if on_off_state[i_switch - 1] == "on":
                on_off_counter += 1
        if on_off_counter % 2 != is_on_off[ki]:
            break
    else:
        res += 1
    print(res, i)

print(res)

