abc = [int(input()) for i in range(3)]

for i in range(3):
    if abc[i] == max(abc):
        print(1)
    elif abc[i] == min(abc):
        print(3)
    else:
        print(2)
