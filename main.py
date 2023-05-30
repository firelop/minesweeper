import pygame, hud.hud as hud, hud.menu as mnu, game as gm
from consts import *

pygame.init()
pygame.display.set_caption("Démineur")
clock = pygame.time.Clock()
clock.tick(30)
police = pygame.font.Font("fonts/Orbitron.ttf", 36)



while True:
    menu = mnu.Menu(DIFFICULTIES)
    window = menu.load()

    while menu.isLoaded:
        menu.display()
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONUP:
                (x, y) = pygame.mouse.get_pos()

                menu.clic((x, y))
            

        pygame.display.flip()

    if menu.difficulty_selected == "Quitter":
        pygame.quit()
        exit()

    chronometer = hud.Chronometer(window)
    game = gm.Game(window, DIFFICULTIES[menu.difficulty_selected], chronometer)
    chronometer.setup_position()
    chronometer.restart()
    difficulty_select_list = hud.SelectList(
        window, DIFFICULTIES, (cell_size.get() // 2, TOP_SIZE // 2), (130, TOP_SIZE // 2), game)

    while game.playing:  # Main loops
        hud.render_hud(window, difficulty_select_list, chronometer)

        # Display difficulties
        if difficulty_select_list.open :
            difficulty_select_list.display_difficulties()
        elif game.game_over:
            game.display_game_over()
        elif game.won:
            game.display_win()
        else:
            game.render()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.playing = False
            
            if event.type == pygame.KEYUP:
                if(event.key == pygame.K_SPACE):
                    (x, y) = pygame.mouse.get_pos()
                    game.flag(x, y, event)

            if event.type == pygame.MOUSEBUTTONUP:
                (x, y) = pygame.mouse.get_pos()

                if not difficulty_select_list.open:
                    game.click(x, y, event)

                if event.button == 3:
                    game.flag(x, y, event)
                
                if game.game_over or game.won:
                    game.endGame_clicked((x, y))
                    if game.restart:
                        game = gm.Game(window, game.difficulty, chronometer)
                        game.restart == False
    
                difficulty_select_list.mouse_clic((x, y))
            
            if difficulty_select_list.isClicked:
                game.playing = False
                game = gm.Game(window, DIFFICULTIES[difficulty_select_list.selected_option], chronometer)
                difficulty_select_list.isClicked = False

        pygame.display.flip()

    space_pressed = False

pygame.quit()
