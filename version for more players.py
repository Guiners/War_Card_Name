import random
import numpy as np


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
    licznik = 0
    for j in range(len(list_of_players)):
        print("player", j, "has", len(list_of_players[j]))
        licznik += len(list_of_players[j])
        print("liczba kart", licznik)
        if len(list_of_players[j]) == 0:
            pass

        else:
            stos.append(list_of_players[j][0])
            print('player', j, "put", list_of_players[j][0])
            list_of_players[j].pop(0)
    #print(list_of_players)
    winers.append(str("Player" + str(j)))
    for w in winers:
        if w not in winers2:
            winers2.append(w)

    copy_stos = stos.copy()
    copy_stos.sort()
    print(copy_stos[0])

    if len(copy_stos) > 1:
        if copy_stos[0][0] != copy_stos[1][0]:
            war.append(stos.index(copy_stos[0]))
            print("war", war)   #tu jest ewidentnie jakis problem
            print('player numer', war, 'lost')
            stos.extend(extra_stos)
            list_of_players[war[0]].extend(stos)
            stos = []

        else:
            war.append(stos.index(copy_stos[0]))
            print("war", war)   #tu jest ewidentnie jakis problem

            print("WAR APPEND2")
            for k in range(len(stos)):
                if k != 0:  #ten warunek ma jakis problem
                    if copy_stos[0][0] == copy_stos[k][0]:
                        index2 = stos.index(copy_stos[k])
                        print("war", war)   #tu jest ewidentnie jakis problem

                        war.append(index2)
                        print("war", war)   #tu jest ewidentnie jakis problem

                        print("WAR APPEND3")

                        #mamy juz graczy ktorzy sa zakwalifikowani do wojny to znaczy do kolejnej rozgrywki
                war_copy = war.copy()
    else:
        pass

        print("Battle between", war_copy, "players just begins") #nie wyswietla dwoch zawodnikow
        for i in range(len(war_copy)):
            war[i] = list_of_players[i]
            #print(war)






        fight(war,stos)
    #print("Winers in sequence",winers2)
    #fight(war, stos)
    return winers2









        #tutaj trzeba sprawdzic jaka karta jest najnizsza z copy_stos i jaki jest jej index na liscie stos. na tej podstawie mozna
        #stwierdzic ktory gracz przegral. Co wiecej trzeba rozwazyc opcje wojny(dwie karty o tej samej wartosci) i stworzyc rekurencje
        #zeby tylko tamta dwojka wrzucila nowe kart do stosu. czyli trzeba stworzyc stos zapasowy czyli taki w ktorym skladowane bylyby
        #karty z poprzedniej rozygrywki aby przegrany gracz z wojny dobral je przy przegranej wojnie.




card_deck = deck_making()
players = dealing(card_deck, number_of_players)
print(type(number_of_players))
while number_of_players > 1:
    winers2 = fight(players)

print("Winers in sequence", winers2)

#while len(player1) != 0 or len(player2) != 0:


#print("p1 ma tyle kart w deku", len(player1))
#print("p2 ma tyle kart w deku", len(player2))
