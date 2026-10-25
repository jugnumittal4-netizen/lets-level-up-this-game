import pygame
import random
SCREEN_WIDTH,SCREEN_HEIGHT = 500,400
MOVEMENT_SPEED = 5
FONT_SIZE = 72
pygame.init()
background = pygame.transform.scale(pygame.image.load("MBG.PNG"), (SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.SysFont("The Times New Roman", FONT_SIZE)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
       super().__init__()
       self.image = pygame.Surface([width, height])
       self.image.fill(pygame.Color("DodgerBlue"))
       pygame.draw.rect(self.image, pygame.Color(color), [0, 0, width, height])
       self.rect = self.image.get_rect()
    

    def move(self, x_change, y_change):
        self.rect.x = max(min(x_change, SCREEN_WIDTH - self.rect.width), 0)
        self.rect.y = max(min(y_change, SCREEN_HEIGHT - self.rect.height), 0)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Collision")
all_sprites = pygame.sprite.Group()
sprite1 = Sprite(pygame.Color("Red"), 20, 30)
sprite1.rect.x = random.randint(0, SCREEN_WIDTH - sprite1.rect.width)
sprite1.rect.y = random.randint(0, SCREEN_HEIGHT - sprite1.rect.height) 
all_sprites.add(sprite1)
sprite2 = Sprite(pygame.Color("black"), 20, 30)
sprite2.rect.x = random.randint(0, SCREEN_WIDTH - sprite1.rect.width)
sprite2.rect.y = random.randint(0, SCREEN_HEIGHT - sprite1.rect.height) 
all_sprites.add(sprite2)
running,won = True,False
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
            running = False
    if not won:
        keys= pygame.key.get_pressed()
        x_change =(keys[pygame.K_RIGHT]-keys[pygame.K_LEFT])*MOVEMENT_SPEED
        y_change =(keys[pygame.K_DOWN]-keys[pygame.K_UP])*MOVEMENT_SPEED
        sprite1.move(x_change,y_change)
        if sprite1.rect.colliderect(sprite2.rect):
            all_sprites.remove(sprite2)
            won = True
    screen.blit(background,(0,0))
    all_sprites.draw(screen)
    if won:
        win_text = font.render("you Win!",True,pygame.Color("black"))
        screen.blit(win_text,((SCREEN_WIDTH - win_text.width())))//2, (SCREEN_HEIGHT - win_text.hieght())//2
    pygame.display.flip()
    clock.tick(90)
pygame.quit


        



