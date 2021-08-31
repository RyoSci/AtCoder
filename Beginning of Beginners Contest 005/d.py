import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

x = int(input())
sounds = ["Do", "Re", "Mi", "Fa", "So", "Ra", "Si"]
Hz = [264, 297, 330, 352, 396, 440, 495]

for i in range(7):
    y = Hz[i]
    while 1 <= y:
        if x == y:
            print(sounds[i])
            exit()
        if y % 2 != 0:
            break
        else:
            y //= 2

    y = Hz[i]
    while y <= 10**9:
        if x == y:
            print(sounds[i])
            exit()
        y *= 2
