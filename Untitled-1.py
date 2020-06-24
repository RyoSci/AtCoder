# x=10**18
# y=7
# print(x^y)
a="2 3 4 5 6 7"
a=map(int,a.split())
b=0
for i in a:
    b=b^i
    print(b)