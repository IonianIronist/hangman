import sys
import pygame

pygame.init()

size = width, height = 800, 600
white = (255, 255, 255)
black = (0, 0, 0)

screen = pygame.display.set_mode(size)
screen.fill(white)
errors = 0

drawings = []
for i in range(7):
    drawings.append(r"TOTAL_PATH\assets\hangman_{}.bmp".format(i))
image = pygame.image.load(drawings[0])

letters = list("abcdefghijklmnopqrstuvwxyz")
seeked_word = list("verrydifficaultword")
found_letters = ['_' for _ in seeked_word]
used_letters = []
font = pygame.font.Font('freesansbold.ttf', 40)
found_text = [font.render(x, True, black, white) for x in found_letters]
text_rects = [letter.get_rect() for letter in found_text]
game_over = font.render('GAME OVER', True, white, black)
game_over_rect = game_over.get_rect()
game_over_rect.center = (400, 300)
while True:
    if errors < 7:
        for i in range(len(text_rects)):
            text_rects[i].center = (400 + 25 * i, 450)
        screen.fill(white)
        screen.blit(image, (0, 0))
        for text, rect in zip(found_text, text_rects):
            screen.blit(text, rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                letter = event.unicode.lower()
                if letter in letters and letter in seeked_word:
                    for i in range(len(seeked_word)):
                        if letter == seeked_word[i]:
                            found_text[i] = font.render(letter, True, black, white)
                            text_rects[i] = found_text[i].get_rect()
                else:
                    errors += 1
                    if errors < 7:
                        image = pygame.image.load(drawings[errors])
    else:
        screen.fill(black)
        screen.blit(game_over, game_over_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            else:
                pass
    pygame.display.update()
