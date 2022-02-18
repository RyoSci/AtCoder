na, nb = map(int, input().split())
a = set(input().split())
b = set(input().split())

intersection = a & b
union = a | b
print(len(intersection) / len(union))