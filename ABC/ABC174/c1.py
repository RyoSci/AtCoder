k = int(input())
mod = 7 % k
counter = 1
memo = 1
mod_map = set()
mod_map.add(mod)
while mod != 0:
    memo = ((memo % k) * (10 % k)) % k
    mod = (mod + 7 * memo) % k
    if mod not in mod_map:
        mod_map.add(mod)
    else:
        counter = -1
        break
    counter += 1
    if mod == 0:
        break
print(counter)
