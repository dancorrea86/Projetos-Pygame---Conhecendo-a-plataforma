import pygame, sys

class Duck(pygame.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()

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
        print(self.rect.y, self.rect.x)

pygame.init()
screen_x = 720
screen_y = 400
screen = pygame.display.set_mode((screen_x,screen_y))
pygame.mouse.set_visible(False)

duck = Duck("Conhecendo a movimentação\Assets\Idle_002-1.png")
duck_group = pygame.sprite.Group()
duck_group.add(duck)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    screen.fill((205, 227, 238))
    duck_group.draw(screen)
    duck_group.update()

    pygame.draw.rect(screen, "black", (0,0,20,400), 20)
    pygame.draw.rect(screen, "black", (700,0,20,400), 20)
    pygame.draw.rect(screen, "black", (0,380,720,20), 20)
    pygame.draw.rect(screen, "black", (0,0,720,20), 20)

    pygame.display.flip()
    clock.tick(60)       