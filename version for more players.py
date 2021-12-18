import random
import numpy as np
import time

while True:
    number_of_players = int(input("Enter number of players:(At least 2 players)"))
    if number_of_players > 1:
        break


def deck_making():
    ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    colors = ["Trefl", "Karo", "Kier", "Pik"]
    deck = []
    card = []
    number_of_decks = int(np.ceil(number_of_players / 6))
    for iteration in range(number_of_decks):
        for color in colors:
            for rank in ranks:
                card.append(rank)
                card.append(color + str(iteration))
                deck.append(card)
                card = []
    random.shuffle(deck)
    return deck


def dealing(deck, number_of_players):
    list_of_players = []
    for number in range(number_of_players):
        list_of_players.append([])

    while len(deck) != 0:
        for number in range(number_of_players):
            if len(deck) != 0:
                list_of_players[number].append(deck[0])
                deck.pop(0)
            else:
                break
    return list_of_players


def fight(
    list_of_players,
    extra_stos=[],
    winners2=[],
):
    war = []
    stos = []
    winners = []
    in_game = []
    for number in range(len(list_of_players)):
        if len(list_of_players[number]) == 0:
            winners2.append(str("Player" + str(number)))
            pass

        else:
            in_game.append(number)
            stos.append(list_of_players[number][0])
            print("player", number, "put", list_of_players[number][0])
            list_of_players[number].pop(0)
    copy_stos = stos.copy()
    copy_stos.sort()
    if len(copy_stos) > 1:
        if copy_stos[0][0] != copy_stos[1][0]:
            war.append(stos.index(copy_stos[0]))
            print("player numer", war, "lost")
            stos.extend(extra_stos)
            list_of_players[in_game[war[0]]].extend(stos)
            stos = []

        else:
            war.append(stos.index(copy_stos[0]))
            for card_number in range(len(stos)):
                if card_number != 0:
                    if copy_stos[0][0] == copy_stos[card_number][0]:
                        index2 = stos.index(copy_stos[card_number])
                        war.append(index2)
                        war_copy = war.copy()
                        for iteration in range(len(war_copy)):
                            war[iteration] = list_of_players[iteration]
            fight(war, stos)

    else:
        stos.extend(extra_stos)
        list_of_players[in_game[0]].extend(stos)
        stos = []

    for winner in winners2:
        if winner not in winners:
            winners.append(winner)

    return winners


card_deck = deck_making()
players = dealing(card_deck, number_of_players)

while True:
    winners2 = fight(players)
    if len(winners2) == number_of_players:
        break
    time.sleep(1)

print("Winers in sequence", winners2)
