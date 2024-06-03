import pygame

pygame.init()

SCREEN_WIDTH =800
SCREEN_HEIGHT=int(SCREEN_WIDTH*0.8)

screen =pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Shooter')


#set timedelay
clock = pygame.time.Clock()
FPS = 60

#player action
moving_left = False
moving_right = False


BG = (144,201,120)
BL = (0, 0, 255)
RED = (255, 0, 0)

def draw_bg():
    screen.fill(BG)

class Soldier(pygame.sprite.Sprite):
    def __init__(self,color,x,y,scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.direction = 1
        self.flip = False
        img = pygame.Surface((25, 25))  # 50x50 크기의 Surface 생성
        img.fill(color)  # 파란색으로 채우기
        self.image = pygame.transform.scale(img,(int(img.get_width()*scale),int(img.get_height()*scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


    def move(self,moving_left,moving_right):
        #reset move
        dx=0
        dy=0


        #assign move
        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1
        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1


        self.rect.x += dx
        self.rect.y += dy

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False),self.rect)

player = Soldier(BL,200,200,3,5)
enemy = Soldier(RED,400,200,3,5)

run=True
while run:

    clock.tick(FPS)

    draw_bg()

    player.draw()
    enemy.draw()

    player.move(moving_left,moving_right)

    for event in pygame.event.get():
        #quit game
        if event.type ==pygame.QUIT:
            run=False
        #key press
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_ESCAPE:
                run - False

        #key release
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
    
    pygame.display.update()
    
pygame.quit()