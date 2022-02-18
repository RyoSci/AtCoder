n, va, vb, l = map(int, input().split())

# for i in range(n):
#     time = l / va
#     l = vb * time

# print(l)

def f(n, l):
    if n == 0:
        return l
    time = l / va
    return f(n - 1, vb * time)

print(f(n, l))
