num=int(input())
moji_set=set()
for i in range(num):
    line=input()
    moji_set.add(line)
print(len(moji_set))