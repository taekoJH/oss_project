import pygame

pygame.init()

SCREEN_WIDTH =800
SCREEN_HEIGHT=int(SCREEN_WIDTH*0.8)

screen =pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Shooter')


#set timedelay
clock = pygame.time.Clock()
FPS = 60

BG = (144,201,120)
BL = (0, 0, 255)
RED = (255, 0, 0)

def draw_bg():
    screen.fill(BG)


run=True
while run:
    for event in pygame.event.get():
        #quit game
        if event.type ==pygame.QUIT:
            run=False
    
    pygame.display.update()
    
pygame.quit()