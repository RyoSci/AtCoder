n = int(input())
cards = list("123456")
n %= 30
counter = 0
for i in range(6):
    for j in range(5):
        if counter == n:
            break
        cards[j], cards[j + 1] = cards[j + 1], cards[j]
        counter += 1

print("".join(cards))
