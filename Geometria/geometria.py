import pygame, random, math

class Ponto(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.color = "red"
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        self.hipotenusa = 0
    
    def defineDistancia(self, mouse_pos):
        self.hipotenusa = hipotenusa(self.rect.center, mouse_pos)

    def update(self):
        self.image.fill(self.color)


def hipotenusa(pontoNum_1, pontoNum_2):
    catetoUm = pontoNum_1[0] - pontoNum_2[0]
    catetoDois = pontoNum_1[1] - pontoNum_2[1]
    hipo = math.sqrt((catetoUm ** 2) + (catetoDois ** 2))
    return hipo

# Genaral setup
pygame.init()
clock = pygame.time.Clock()

# Game screnn
screen_x = 1280
screen_y = 720
screen = pygame.display.set_mode((screen_x,screen_y))

# GameStatus
game_over = True
restart = True
running = True

# Pontos
pontos_group = pygame.sprite.Group()
for pontos in range(30):
    new_ponto = Ponto(random.randrange(25,1200), random.randrange(25, 660))
    pontos_group.add(new_ponto)

pintou = False

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    
    screen.fill((255, 255, 255))

    # Eixo X
    startX = 20; startY = 20; endX = 20; endY = 700; width = 4
    pygame.draw.line(screen, "black", (startX, startY), (endX, endY), width)
    pygame.draw.line(screen, "black", (startX + 100, startY), (endX + 100, endY), width - 3)
    pygame.draw.line(screen, "black", (startX + 200, startY), (endX + 200, endY), width - 3)
    pygame.draw.line(screen, "black", (startX + 300, startY), (endX + 300, endY), width - 3)
    pygame.draw.line(screen, "black", (startX + 400, startY), (endX + 400, endY), width - 3)
    pygame.draw.line(screen, "black", (startX + 500, startY), (endX + 500, endY), width - 3)
    pygame.draw.line(screen, "black", (startX + 600, startY), (endX + 600, endY), width - 3)
    pygame.draw.line(screen, "black", (startX + 700, startY), (endX + 700, endY), width - 3)
    pygame.draw.line(screen, "black", (startX + 800, startY), (endX + 800, endY), width - 3)
    pygame.draw.line(screen, "black", (startX + 900, startY), (endX + 900, endY), width - 3)
    pygame.draw.line(screen, "black", (startX + 1000, startY), (endX + 1000, endY), width - 3)
    pygame.draw.line(screen, "black", (startX + 1100, startY), (endX + 1100, endY), width - 3)
    pygame.draw.line(screen, "black", (startX + 1200, startY), (endX + 1200, endY), width - 3)
    
    ey_startX = 20; ey_startY = 700; ey_endX = 1240; ey_endY = 700; ey_width = 4
    pygame.draw.line(screen, "black", (ey_startX, ey_startY), (ey_endX, ey_endY), ey_width)

    pontos_group.draw(screen)

    if(pygame.mouse.get_pressed()[0] == True):
        for ponto in pontos_group:
            ponto.defineDistancia(pygame.mouse.get_pos())
        
        pontoMin = min(pontos_group, key= lambda y: y.hipotenusa)
        pontoMin.color = "green"
        pontos_group.update()
        
            


    pygame.display.flip()
    clock.tick(60)   