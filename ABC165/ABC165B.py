x=int(input())
s=100
for i in range(1000000000000000000):
    s=int(s*1.01)
    if s>=x:
        print(i+1)
        break