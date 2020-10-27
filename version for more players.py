import random
import numpy as np
import time

while True:
    number_of_players = int(input("Enter number of players:(At least 2 players)"))
    if number_of_players > 1:
        break


def deck_making():
    ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    color = ["Trefl", "Karo", "Kier", "Pik"]
    deck = []
    card = []
    number_of_decks = int(np.ceil(number_of_players / 6))
    for i in range(number_of_decks):
        for k in color:
            for j in ranks:
                card.append(j)
                card.append(k+str(i))
                deck.append(card)
                card = []
    random.shuffle(deck)
    return deck




def dealing(deck, number_of_players):
    list_of_players = []
    for i in range(number_of_players):
        list_of_players.append([])

    while len(deck) != 0:
        for i in range(number_of_players):
            if len(deck) != 0:
                list_of_players[i].append(deck[0])
                deck.pop(0)
            else:
                break
    return list_of_players




def fight(list_of_players, extra_stos = [], winers = [],):
    war = []
    stos = []
    winers2 = []
    #licznik = 0
    in_game = []
    for j in range(len(list_of_players)):
        #licznik += len(list_of_players[j])
        #print('a', list_of_players[j])
        if len(list_of_players[j]) == 0:
            winers.append(str("Player" + str(j)))
            pass

        else:
            print("player", j, "has", len(list_of_players[j]))
            in_game.append(j)
            #print("players in game",in_game)
            stos.append(list_of_players[j][0])
            print('player', j, "put", list_of_players[j][0])
            list_of_players[j].pop(0)
    #print("liczba kart", licznik)
    copy_stos = stos.copy()
    copy_stos.sort()
    if len(copy_stos) > 1:
        if copy_stos[0][0] != copy_stos[1][0]:
            war.append(stos.index(copy_stos[0]))
            print('player numer', war, 'lost')
            stos.extend(extra_stos)
            list_of_players[in_game[war[0]]].extend(stos)
            stos = []

        else:
            war.append(stos.index(copy_stos[0]))
            for k in range(len(stos)):
                if k != 0:
                    if copy_stos[0][0] == copy_stos[k][0]:
                        index2 = stos.index(copy_stos[k])
                        war.append(index2)
                        war_copy = war.copy()
                        for i in range(len(war_copy)):
                            war[i] = list_of_players[i]
            fight(war,stos)

    else:
        stos.extend(extra_stos)
        list_of_players[in_game[0]].extend(stos)
        stos = []

    for w in winers:
        if w not in winers2:
            winers2.append(w)

    return winers2


card_deck = deck_making()
players = dealing(card_deck, number_of_players)
#print(type(number_of_players))
while True:
    winers3 = fight(players)
    if len(winers3) == number_of_players:
        break
    time.sleep(1)

print("Winers in sequence", winers3)
