n = int(input())
anaglram_map = dict()


for i in range(n):
    line = input()
    line = sorted(line)
    line = str(line)
    if line not in anaglram_map:
        anaglram_map[line] = 1
    else:
        anaglram_map[line] += 1

couter = 0
for value in anaglram_map.values():
    if value >= 2:
        couter += value * (value - 1) // 2
print(couter)
