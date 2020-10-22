import random

number_of_players = int(input())


ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
color = ["Trefl", "Karo", "Kier", "Pik"]
deck = []
card = []
player1 = []
player2 = []

for k in color:
    for j in ranks:
        card.append(j)
        card.append(k)
        deck.append(card)
        card = []

random.shuffle(deck)

while len(deck) != 0:
    k = len(deck)
    if k % 2 == 0:
        player1.append(deck[0])
    else:
        player2.append(deck[0])
    deck.pop(0)


def fight(d1, d2, n = 0, stos = []):
    print("p1 card", d1[n][0], "amount cards in deck", len(d1))
    print("p2 card", d2[n][0], "amount cards in deck", len(d2))
    #print(d1,d2)
    if d1[n][0] < d2[n][0]:
        stos.append(d1[n])
        stos.append(d2[n])
        #print(stos)
        d1.pop(0)
        d2.pop(0)
        d2.extend(stos)
        stos.clear()
        print("p2 win")

    elif d1[n][0] > d2[n][0]:
        stos.append(d1[n])
        stos.append(d2[n])
        #print(stos)
        d1.pop(0)
        d2.pop(0)
        d1.extend(stos)
        stos.clear()
        print("p1 win")

    elif d1[n][0] == d2[n][0]:
        while d1[n][0] == d2[n][0]:
            stos.append(d1[n])
            stos.append(d2[n])
            #print(stos)
            d1.pop(0)
            d2.pop(0)
            #print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            fight(d1, d2, n, stos)

    return d1, d2

while len(player1) != 0 or len(player2) != 0:
    player1, player2 = fight(player1, player2)

print("p1 ma tyle kart w deku", len(player1))
print("p2 ma tyle kart w deku", len(player2))
