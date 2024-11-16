import pygame
import random
import os
import math

pygame.init()

# variables
WIDTH = 800
HEIGHT = 500
WHITE = (255,255,255)
BLACK = (0,0,0)
RADIOUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIOUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65
FPS = 60
clock = pygame.time.Clock()
run = True
images = []
LETTER_FONT = pygame.font.SysFont('comicsans',30)
WORD_FONT = pygame.font.SysFont('comicsans',40)
TITLE_FONT = pygame.font.SysFont('comicsans',50)
hangman_status = 0
words=["APPLE", "BANANA", "ORANGE", "GRAPE", "MANGO", "PINEAPPLE", "STRAWBERRY", "BLUEBERRY", "WATERMELON", "CHERRY"]
word = random.choice(words)
guessed = []

for i in range(26):
    x = startx + GAP * 2 + ((RADIOUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIOUS * 2))
    letters.append([x,y, chr(A + i), True])

# Set up display
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game :)")

# Load images

for i in range(6):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)



def draw():
    win.fill(WHITE)

    text = TITLE_FONT.render("HANGMAN", 1, BLACK)
    win.blit(text, (text.get_width()/2, 20))
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (400, 200))

    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIOUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))
    win.blit(images[hangman_status],(150,100))
    pygame.display.update()

def display_msg(msg):
    win.fill(WHITE)
    text = WORD_FONT.render(msg, 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)

# Main game loop    
while run:
    clock.tick(FPS)
    draw()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:  
            m_x, m_y = pygame.mouse.get_pos()
            for  letter in letters:
                x, y, ltr, visible =letter
                if visible:
                    dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                    if dis < RADIOUS:
                        letter[3] = False
                        guessed.append(ltr)
                        if ltr not in word:
                            hangman_status += 1
    draw()
    
    won = True
    for letter in word:
        if letter not in guessed:
            won = False
            break

    if won:
        
        display_msg("CONGRATULATIONS, YOU WON!!")
        break

    if hangman_status == 6:
        
        display_msg("OH NO, YOU LOST!!")
        break

    # Update the display
    pygame.display.update()

pygame.quit()