import pygame

#Creating Game window
game_win=pygame.display.set_mode((1200,600))

#Creating Game Title
pygame.display.set_caption("My First Game ")

#Game specific variable
exit_game=False     #agr False hai to game chalta rahega agr true hai to band ho jayga
game_over=False

#Creating a game loop: Game window ko hold krke rakhega jb tk game chal rhi hai
while not exit_game:
    # pass
    for event in pygame.event.get():    #records every event in our game
        # print(event)
        if event.type==pygame.QUIT:   #if this event takes place, then game exits to main screen
            exit_game=True

        if event.type == pygame.KEYDOWN:                    # checks if any key is pressed or not
            if event.key == pygame.K_RIGHT:                     # ye check krta hai ki kya sahi key dabi??
                print('Yess, Its the right arrow key')





pygame.quit()
quit()

























