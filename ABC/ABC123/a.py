n = 5 
antena = []
for i in range(n):
    antena.append(int(input()))

antena.sort()
k = int(input())

if antena[-1] - antena[0] <= k:
    print("Yay!")
else:
    print(":(")