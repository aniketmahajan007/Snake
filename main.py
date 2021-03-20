import pygame
from pygame.math import Vector2
import sys, random


class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)

    def draw_snake(self):
        for block in self.body:
            x = block.x * cell_size
            y = block.y * cell_size
            snake_block = pygame.Rect(x, y, cell_size, cell_size)
            pygame.draw.rect(screen, pygame.Color('red'), snake_block)

    def move_snake(self):
        body_c = self.body[:-1]
        body_c.insert(0, body_c[0] + self.direction)
        self.body = body_c

    def update_snake(self, Vec):
        self.body.append(Vec)

    def reset(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]


class FOOD:
    def __init__(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

    def make_food(self):
        f = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size)
        screen.blit(insect, f)
        # pygame.draw.rect(screen, pygame.Color('blue'), f)

    def generate_new_food(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)


class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.food = FOOD()
        self.score = 0

    def update(self):
        self.snake.move_snake()
        self.check_collison()
        self.check_walls()
        self.check_snake_collision()
        self.draw_score()



    def gui(self):
        self.food.make_food()
        # Blit for block image transfer and x & y dimension to put surface
        self.snake.draw_snake()

    def snake_movement(self):
        if event.key == pygame.K_UP:
            if main_game.snake.direction.y != 1:
                self.snake.direction = Vector2(0, -1)
        if event.key == pygame.K_RIGHT:
            if main_game.snake.direction.x != -1:
                self.snake.direction = Vector2(1, 0)
        if event.key == pygame.K_LEFT:
            if main_game.snake.direction.x != 1:
                self.snake.direction = Vector2(-1, 0)
        if event.key == pygame.K_DOWN:
            if main_game.snake.direction.y != -1:
                self.snake.direction = Vector2(0, 1)

    def check_collison(self):
        if self.snake.body[0] == self.food.pos:
            self.food.generate_new_food()
            self.snake.update_snake(self.food.pos)
            self.score = self.score + 1

    def game_over(self):
        self.snake.reset()
        self.score = 0

    def check_walls(self):
        if self.snake.body[0].x < 0 or self.snake.body[0].y < 0 or self.snake.body[0].x > cell_number - 1 or self.snake.body[0].y > cell_number - 1:
            self.game_over()

    def check_snake_collision(self):
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def draw_score(self):
        textsurface = pygame.font.SysFont(None, 60).render(str(self.score), True, pygame.Color('red'))
        screen.blit(textsurface, (60, 60))


pygame.init()
pygame.font.init()
cell_size = 20
cell_number = 40
insect = pygame.image.load("graphics/insect.png")
# screen of game
screen = pygame.display.set_mode((cell_number * cell_size, cell_size * cell_number))

# setting speed of prog or frames of games
clock = pygame.time.Clock()

# developing shapes
test_rect = pygame.Rect(100, 200, 100, 100)
Screen__Updater = pygame.USEREVENT
pygame.time.set_timer(Screen__Updater, 100)
game_font = pygame.font.Font(None, 25)

main_game = MAIN()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == Screen__Updater:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            main_game.snake_movement()

    # Adding color in screen can be done in 2 ways rgb or color object
    screen.fill((165, 215, 70))
    main_game.gui()
    pygame.display.update()
    # frame set
    clock.tick(60)

'''
x = 0
y = 0
touchx = False
touchy = False
while 1:
    if x > 300:
        touchx = True
    if x < 0:
        touchx = False
    if touchx:
        x = x - 1
    else:
        x = x + 0.2

    if y > 300:
        touchy = True
    if y < 0:
        touchy = False
    if touchy:
        y = y - 0.7
    else:
        y = y + 0.5
    # draw elements
    print(x,y)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Adding color in screen can be done in 2 ways rgb or color object
    screen.fill((165, 215, 70))
    # Blit for block image transfer and x & y dimension to put surface
    screen.blit(test_surface, (x, y))
    pygame.display.update()
    # frame set
    clock.tick(144)
'''
