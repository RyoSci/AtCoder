n=int(input())
array=[""]*n

for i in range(5):
    line=input()
    for j in range(n):
        array[j]+=line[4*j:4*(j+1)]
# print(array)

res=[""]*n
zero_nine=['.###.#.#.#.#.#.#.###', '..#..##...#...#..###', '.###...#.###.#...###', '.###...#.###...#.###', '.#.#.#.#.###...#...#', '.###.#...###...#.###', '.###.#...###.#.#.###', '.###...#...#...#...#', '.###.#.#.###.#.#.###', '.###.#.#.###...#.###']
for i in range(len(array)):
    for j in range(len(zero_nine)):
        if array[i]==zero_nine[j]:
            res[i]=str(j)
            break
print("".join(res))