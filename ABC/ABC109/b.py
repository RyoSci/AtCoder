n = int(input())
w = input()
double_set = set()
double_set.add(w)
finish_str = w[-1]

for i in range(1, n):
    w = input()
    if w not in double_set and w[0] == finish_str:
        double_set.add(w) 
        finish_str = w[-1]
    else:
        print("No")
        break
else:
    print("Yes")