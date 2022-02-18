k = int(input())
mod = 7 % k
counter = 1
memo = 1
mod_map = set()
mod_map.add(mod)
while mod != 0:
    mod = ((mod * 10) % k + 7) % k
    if mod not in mod_map:
        mod_map.add(mod)
    else:
        counter = -1
        break
    counter += 1
    if mod == 0:
        break
print(counter)
