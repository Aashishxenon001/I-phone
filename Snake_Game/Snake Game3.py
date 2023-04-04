import pygame
import random

pygame.init()

#COlours
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)


screen_width=900
screen_height=600

pygame.display.set_caption("Snakey GAME")
# pygame.display.update()

#Creating Game window
game_win=pygame.display.set_mode((screen_width,screen_height))

#Game specific variable
exit_game=False     #agr False hai to game chalta rahega agr true hai to band ho jayga
game_over=False
snake_x=245
snake_y=177
velocity_x=0
velocity_y=0
food_x= random.randint(0,screen_width)
food_y= random.randint(0,screen_height)
snake_size=20
clock = pygame.time.Clock()
fps=60

# GAME LOOP
while not exit_game:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:  # if this event takes place, then game exits to main screen
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x = 2
                velocity_y = 0

            if event.key == pygame.K_LEFT:
                velocity_x=-2
                velocity_y = 0

            if event.key == pygame.K_UP:
                velocity_y=-2
                velocity_x = 0

            if event.key == pygame.K_DOWN:
                velocity_y=2
                velocity_x = 0

    snake_x = snake_x + velocity_x
    snake_y = snake_y + velocity_y

    game_win.fill(white)
    #my snake
    pygame.draw.rect(game_win, black,[snake_x,snake_y,snake_size,snake_size])

    # my snake food
    pygame.draw.rect(game_win, red,[food_x,food_y,snake_size,snake_size])

    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()









