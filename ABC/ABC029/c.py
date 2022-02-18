import itertools
n = int(input())
abc = "abc"
for i in itertools.product(abc, repeat=n):
    print("".join(i))
