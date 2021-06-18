import pygame
import sys
import random
import math
import time
import config

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(config.musicfile)
pygame.mixer.music.set_volume(config.volume)
speed = config.speed
score = 0
win_x = 600
win_y = 500
tempr = 100
font = pygame.font.SysFont(None, 24)
pygame.display.set_caption('OSU! clone by Prabesh Shrestha')
screen = pygame.display.set_mode((win_x, win_y))
clock = pygame.time.Clock()
BACKGROUND = (252, 204, 174)
circle_exists = False
CIRCLECOLOR = (0, 168, 151)
CIRCLERADIUS = 50
animatedCircle = (235, 52, 192)

def checkandcollect():
    global circle_exists
    global score
    mouse_x, mouse_y = pygame.mouse.get_pos()
    print(mouse_x,mouse_y)
    if (collision(mouse_x, mouse_y, circle_x, circle_y, 50)):
        print("colided")
        score +=10
        circle_exists = False
    
def drawcircle(circle_x, circle_y):
    pygame.draw.circle(screen, CIRCLECOLOR, (circle_x, circle_y), 50)
    
 
def text_objects(text, font):
    textSurface = font.render(text, True, (0, 0, 0))
    return textSurface, textSurface.get_rect()
 

def collision(x1,y1,x2,y2,offset):
    dis = math.sqrt(math.pow(x2-x1, 2) + math.pow(y2-y1,2))
    if dis<offset:
        return True
    else:
        return False
def introscreen():
    screen.fill((255,255,255))
    largeText = pygame.font.Font('freesansbold.ttf',25)
    TextSurf, TextRect = text_objects("Osu clone", largeText)
    TextRect.center = ((win_x/2),(win_y/2))
    screen.blit(TextSurf, TextRect)  
    TextSurf, TextRect = text_objects("hover over the circle and press x to hit it", largeText)
    TextRect.center = ((win_x/2),(win_y/2 + 50))
    screen.blit(TextSurf, TextRect)
    pygame.display.update()
    screen.fill((0,0,0))

    time.sleep(5)


introscreen()
gameloop = True
pygame.mixer.music.play()
while gameloop:

    screen.fill(BACKGROUND)

    img = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(img, (20, 20))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                print("A key was pressed!")
                checkandcollect()



    if not(circle_exists):
        circle_x = random.randint(CIRCLERADIUS,win_x - CIRCLERADIUS)
        circle_y = random.randint(CIRCLERADIUS,win_y - CIRCLERADIUS)
        circle_exists = True
        tempr = 100


    drawcircle(circle_x, circle_y)
    pygame.draw.circle(screen, animatedCircle, (circle_x, circle_y), tempr, 4)
    tempr -= speed
    if tempr < 50:
        circle_exists = False
        score -=10
    print(score)
    speed+= config.difficulty
    pygame.display.update()
    clock.tick(120)