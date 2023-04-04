import pygame
# import random

pygame.init()

#Colours
white=(255,255,255)
black=(0,0,0)


screen_width = 600
screen_height=800

pygame.display.set_caption("Balloon GAME")

#Creating Game window
game_win=pygame.display.set_mode((screen_width,screen_height))


#Game specific variable
exit_game=False     #agr False hai to game chalta rahega agr true hai to band ho jayga
game_over=False
gun_x = 530
gun_y = 177
velocity_x = 0
velocity_y = 0

gun_size = 50
clock = pygame.time.Clock()
fps = 60

while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                velocity_y = -4
                velocity_x = 0

            if event.key == pygame.K_DOWN:
                velocity_y = 4
                velocity_x = 0

            if event.key == pygame.K_SPACE:
                velocity_y = 0
                velocity_x = 0

            if gun_y == 650 or gun_y == 80:
                velocity_y = 0
                velocity_x=0




    gun_x = gun_x + velocity_x
    gun_y = gun_y + velocity_y

    # if gun_y = 650:# or gun_y = 80:
    #     velocity_y=0
    # else:
    #     gun_x = gun_x + velocity_x
    #     gun_y = gun_y + velocity_y

    game_win.fill(white)


    #my gun
    pygame.draw.rect(game_win, black, [gun_x,gun_y,gun_size+15,gun_size])
    pygame.draw.rect(game_win, black, [gun_x-20,gun_y+17,gun_size/2,gun_size/3])

    pygame.display.update()
    clock.tick(fps)



pygame.quit()
quit()















