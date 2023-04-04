import pygame

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
snake_size=10

# GAME LOOP
while not exit_game:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:  # if this event takes place, then game exits to main screen
            exit_game = True

    game_win.fill(white)
    pygame.draw.rect(game_win, black,[snake_x,snake_y,snake_size,snake_size])
    pygame.display.update()

pygame.quit()
quit()









