import pygame, sys

class Duck(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.colisao = pygame.mixer.Sound("Reiniciar Game\Assets\Hit_02.wav")
        self.rect.center = [pos_x, pos_y]

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.top > 0 + 20:
            self.rect.y -= 3
        if keys[pygame.K_s] and self.rect.bottom <= screen_y - 20:
            self.rect.y += 3
        if keys[pygame.K_a] and self.rect.left >= 0 + 20:
            self.rect.x -= 3
        if keys[pygame.K_d] and self.rect.right <= screen_x - 20:
            self.rect.x += 3

    def colisao1(self):
        self.colisao.play()

class Boulder(pygame.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = [400, 200]

class GameOver(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Reiniciar Game\Assets\gameover_tam_2.png")
        self.rect = self.image.get_rect()
        self.rect.center = [360, 100]

class ButtonPlay(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"Reiniciar Game\Assets\botaoPlay.png")
        self.rect = self.image.get_rect()
        self.rect.center = [360, 300]
    

# Genaral setup
pygame.init()
clock = pygame.time.Clock()

# Game screnn
screen_x = 720
screen_y = 400
screen = pygame.display.set_mode((screen_x,screen_y))
background = pygame.image.load(r"Reiniciar Game\Assets\background.png")

# GameStatus
game_over = True
restart = True
running = True

while True:

    if restart:
        # Duck
        duck = Duck(40, 50,"Reiniciar Game\Assets\Idle_002-1.png")
        duck_group = pygame.sprite.Group()
        duck_group.add(duck)

        # Builder
        boulder = Boulder(r"Reiniciar Game\Assets\boulder.png")
        boulder_group = pygame.sprite.Group()
        boulder_group.add(boulder)

        # GameOver
        gameover_img = GameOver()
        gameover_group = pygame.sprite.Group()
        gameover_group.add(gameover_img)

        # ButtonPlay
        button_play = ButtonPlay()
        button_play_group = pygame.sprite.Group()
        button_play_group.add(button_play)

        game_over = False
        restart = False
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    
    if duck.rect.colliderect(boulder.rect) and game_over == False:
        duck.colisao1()
        game_over = True

    screen.fill((205, 227, 238))
    screen.blit(background,(0,0))

    duck_group.draw(screen)
    if game_over == False:
        duck_group.update()

    boulder_group.draw(screen)
    boulder_group.update()

    if game_over == True:
        gameover_group.draw(screen)
        gameover_group.update()
        button_play_group.draw(screen)
        button_play_group.update()

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if button_play.rect.collidepoint(pos):
                restart = True

    pygame.draw.rect(screen, "black", (0,0,20,400), 20)
    pygame.draw.rect(screen, "black", (700,0,20,400), 20)
    pygame.draw.rect(screen, "black", (0,380,720,20), 20)
    pygame.draw.rect(screen, "black", (0,0,720,20), 20)

    pygame.display.flip()
    clock.tick(60)       