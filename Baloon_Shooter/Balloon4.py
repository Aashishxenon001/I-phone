import pygame
import random

pygame.init()

#Colours
white=(255,255,255)
black=(0,0,0)
green=(10, 220, 10)
red=(220,0,0)


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

balloon_x = 40
balloon_y = random.randint(50,screen_height-50)
velocity_x = 0
velocity_y = 0
bullet_x = 520
bullet_y = 202
move_up = False
move_down = False
bullet_ready = False
bullet_group = []

balloon_rad=30
bullet_rad=5
gun_size = 50
clock = pygame.time.Clock()
fps = 60


#Bullets
def shoot(bullets):
    global bullet_ready

    #create bullets
    if bullet_ready:
        bullets.append(pygame.Rect(bullet_x,bullet_y,10,10))
        bullet_ready = False

    #move bullet
    for bullet in bullets:
        bullet.x -= 20
        pygame.draw.rect(game_win,red,bullet)

    #destroy bullet

    #return bullet list
    return bullets



#Game Loop
while not exit_game:
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
            exit_game = True

         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move_up = True

            if event.key == pygame.K_DOWN:
                move_down = True


         elif event.type == pygame.KEYUP:
             if event.key == pygame.K_UP:
                move_up = False


             if event.key == pygame.K_DOWN:
                move_down = False

             if event.key == pygame.K_SPACE:
                bullet_ready = True

    if(move_up):
        gun_y -= 5
        bullet_y -= 5

    elif(move_down):
        gun_y += 5
        bullet_y += 5

    game_win.fill(white)

    #my gun
    pygame.draw.rect(game_win, black, [gun_x,gun_y,gun_size+15,gun_size])
    pygame.draw.rect(game_win, black, [gun_x-20,gun_y+17,gun_size/2,gun_size/3])

    #My Balloon
    pygame.draw.circle(game_win, green, (balloon_x,balloon_y),balloon_rad,20)

    #My Bullets
    pygame.draw.circle(game_win, red, (bullet_x,bullet_y),bullet_rad,0)
    bullet_group = shoot(bullet_group)


    pygame.display.update()
    clock.tick(fps)




pygame.quit()
quit()















