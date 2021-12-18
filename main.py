import sys
import pygame
import random

pygame.init()

# window
screen_width = 1440
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))

# time/fps
clock = pygame.time.Clock()

# lists
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"]
colors = ["Trefl", "Karo", "Kier", "Pik"]
deck = []
card = []
player1 = []
player2 = []
font = pygame.font.SysFont("comicsansms", 72)
text1 = font.render("Player One", True, (41, 58, 162))
text2 = font.render("Player Two", True, (162, 41, 50))
score1 = font.render(("Cards in deck: " + str(len(player1))), True, (41, 58, 162))
score2 = font.render(("Cards in deck: " + str(len(player2))), True, (162, 41, 50))


# making talia
for color in colors:
    for rank in ranks:
        card.append(rank)
        card.append(color)
        deck.append(card)
        card = []

# shuffling deck
random.shuffle(deck)

# deal the cards
while len(deck) != 0:
    color = len(deck)
    if color % 2 == 0:
        player1.append(deck[0])
    else:
        player2.append(deck[0])
    deck.pop(0)

run = True
font = pygame.font.SysFont("comicsans", 30, True)

while run:
    clock.tick(27)

    # which key was pressed
    for event in pygame.event.get():

        # exit game
        if event.type == pygame.QUIT:
            sys.exit(0)

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit(0)

    screen.fill((255, 255, 255))
    screen.blit(text1, (10, 1))
    screen.blit(text2, (1430 - text2.get_width(), 1))
    screen.blit(score1, (10, 800))
    screen.blit(score2, (1430 - score2.get_width(), 800))

    pygame.display.flip()
