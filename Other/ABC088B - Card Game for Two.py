num=int(input())
array=[int(i) for i in input().split()]
array=sorted(array,reverse=True)
alice_bob=[0,0]

for i in range(num):
    alice_bob[i%2]+=array[i]
print(alice_bob[0]-alice_bob[1])