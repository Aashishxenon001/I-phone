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


balloon_y = random.randint(50, screen_height - 50)
balloon_y_speed = random.randint(-2,20)
# balloon=pygame.rect(50,balloon_y,50,50)
balloon_rad = 30
balloon_x = 40

bullet_ready = False
bullet_x = 520
bullet_y = 202
font=pygame.font.SysFont(None,55)
# game_over = False
score = 0
miss = 0
game_over = False

#Score ko screen p show karwaana
def text_screen(text,color,x,y):
    text_screen=font.render(text,True, color)
    game_win.blit(text_screen,[x,y])

# def balloon_dance():
#     global balloon_y
#     global balloon_x
#     global balloon_rad
#
#     pygame.draw.circle(game_win, green, (balloon_x, balloon_y), balloon_rad, 20)
#     balloon_y.y += balloon_y_speed
#     # pygame.draw.rect(game_win,green,balloon)


#Game Loop
def Gameloop():
    # Game specific variable
    exit_game = False  # agr False hai to game chalta rahega agr true hai to band ho jayga
    global game_over
    game_over = False
    gun_x = 530
    gun_y = 180
    balloon_x = 40
    global balloon_y
    global balloon_y_speed_down
    global balloon_y_speed_up
    global bullet_x
    global bullet_y
    move_up = False
    move_down = False
    bullet_group = []
    balloon_rad = 30
    bullet_rad = 5
    global bullet_ready
    gun_size = 50
    clock = pygame.time.Clock()
    fps = 60
    global score
    score = 0
    global miss
    miss =0

    # Bullets
    def shoot(bullets):
        global bullet_ready
        global bullet_x
        global bullet_y
        global score
        global balloon_y
        global miss
        miss =0
        global game_over
        game_over = False



        # create bullets
        if bullet_ready:
            bullets.append(pygame.Rect(gun_x-15, gun_y + 22, 10, 5))
            bullet_ready = False

        # move bullet
        for bullet in bullets:
            bullet.x -= 20
            # bullet.y -= 20
            pygame.draw.rect(game_win, red, bullet)
            miss+=1


            #hit target
            if abs(bullet.x-balloon_x)<30 and abs(bullet.y-balloon_y)<30:
                balloon_y=random.randint(50, screen_height - 50)
                game_over = True
                # score += 1
                # print(score*10)

        return bullets

    while not exit_game:

        if game_over:
            game_win.fill(white)
            text_screen("Game Over!!!", red, 160, (screen_height / 2) - 160)
            text_screen("Press Enter to Continue", red, 60, (screen_height / 2)-100)
            text_screen("Missed Shots : "+str(miss-1), green, 130, (screen_height / 2))

            # text_screen("Missed Shots: ")
            pygame.display.update()

            for event in pygame.event.get():
                # print (event)
                if event.type == pygame.QUIT:  # if this event takes place, then game exits to main screen
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        Gameloop()

        else:
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

                     if event.key == pygame.K_ESCAPE:
                         game_over =True

            if(move_up):
                gun_y -= 5
                bullet_y -= 5

            elif(move_down):
                gun_y += 5
                bullet_y += 5

            if gun_y>screen_height:
                gun_y = 0
                bullet_y = 0

            if gun_y<0:
                gun_y = screen_height
                bullet_y = screen_height

            game_win.fill(white)
            text_screen("Fired Shots: " + str(miss), green, 5, 5)
            #my gun
            pygame.draw.rect(game_win, black, [gun_x,gun_y,gun_size+15,gun_size])
            pygame.draw.rect(game_win, black, [gun_x-20,gun_y+17,gun_size/2,gun_size/3])

            #My Balloon

            pygame.draw.circle(game_win, green, (balloon_x,balloon_y),balloon_rad,20)

            #My Bullets
            pygame.draw.circle(game_win, red, (gun_x-10,gun_y+25),bullet_rad,0)
            bullet_group = shoot(bullet_group)


            pygame.display.update()
            clock.tick(fps)
            
            balloon_y+=balloon_y_speed
            if balloon_y<0:
                balloon_y=800
            if balloon_y>800:
                balloon_y=0



    pygame.quit()
    quit()


Gameloop()












