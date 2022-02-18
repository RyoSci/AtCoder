
n = int(input())
cards = []
n %= 30
l = n // 5 + 1
for i in range(6):
    tmp = l % 6
    if tmp == 0:
        tmp = 6
    cards.append(str(tmp))
    l += 1

for i in range(n % 5):
    cards[i], cards[i + 1] = cards[i + 1], cards[i]
print("".join(cards))
