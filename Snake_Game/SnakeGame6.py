import pygame
import random

pygame.init()

#Colours
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
green=(0,200,0)

font = pygame.font.SysFont(None, 55)
screen_width=900
screen_height=600

pygame.display.set_caption("Snakey GAME")
# pygame.display.update()

#Creating Game window
game_win=pygame.display.set_mode((screen_width,screen_height))


#Score ko screen p show karwaana
def text_screen(text,color,x,y):
    text_screen=font.render(text,True, color)
    game_win.blit(text_screen,[x,y])

def plot_snake(game_win, color, snk_list, snake_size):
    # print(snk_list)
    for x,y in snk_list:
        pygame.draw.rect(game_win, black, [x, y, snake_size, snake_size])



# GAME LOOP
def gameloop():
    # Game specific variable
    exit_game = False  # agr False hai to game chalta rahega agr true hai to band ho jayga
    game_over = False
    snake_x = 245
    snake_y = 177
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(0, screen_width / 2)
    food_y = random.randint(0, screen_height / 2)
    score = 0
    snake_size = 20
    clock = pygame.time.Clock()
    fps = 60
    snk_list = []
    snk_length = 1

    #game start
    while not exit_game:
        if game_over:
            game_win.fill(white)
            text_screen("Game Over!!! Press Enter to Continue",red,150,(screen_height/2)-60)
            for event in pygame.event.get():
                # print (event)
                if event.type == pygame.QUIT:  # if this event takes place, then game exits to main screen
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()



        else:
            for event in pygame.event.get():
                # print (event)
                if event.type == pygame.QUIT:  # if this event takes place, then game exits to main screen
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = 4
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -4
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = -4
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = 4
                        velocity_x = 0

                    if event.key == pygame.K_BACKSPACE:
                        velocity_y = 0
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x-food_x)<15 and abs(snake_y-food_y)<15:
                score+=1
                # print('Score is: ',score*10)
                food_x = random.randint(0, screen_width / 2)
                food_y = random.randint(0, screen_height / 2)
                snk_length+=2

            game_win.fill(white)

            #score print
            text_screen("SCORE: "+ str(score*10), green, 5,5)

            # my snake food
            pygame.draw.rect(game_win, red,[food_x,food_y,snake_size/1.5,snake_size/1.5])

            head=[]
            head.append(snake_x)
            head.append((snake_y))
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]

            # snake eats its own body: GAME OVER!!
            if head in snk_list[:-1]:
                game_over=True


            # snake hits wall: GAME OVER!!
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True


            #SNAKE
            plot_snake(game_win,black,snk_list,snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

gameloop()














