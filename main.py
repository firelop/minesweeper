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
    
                difficulty_select_list.mouse_clic((x, y))

        pygame.display.flip()

    space_pressed = False
    while game.game_over and not space_pressed:
        game.window.fill("black")
        police = pygame.font.Font("fonts/SpaceMono-Regular.ttf", 42)
        txt = police.render("Game over", 0, (255, 255, 255))
        width = game.window.get_width() // 2
        height = game.window.get_width() // 2
        
        game.window.blit(txt, (width-txt.get_width()//2, height-txt.get_height()//2))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.playing = False

            if event.type == pygame.KEYUP:
                space_pressed = event.key == pygame.K_SPACE
                    
    while game.won and not space_pressed:
        game.window.fill("black")
        police = pygame.font.Font("fonts/SpaceMono-Regular.ttf", 42)
        txt = police.render("You won !", 0, (255, 255, 255))
        width = game.window.get_width() // 2
        height = game.window.get_width() // 2
        
        game.window.blit(txt, (width-txt.get_width()//2, height-txt.get_height()//2))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.playing = False

            if event.type == pygame.KEYUP:
                space_pressed = event.key == pygame.K_SPACE

pygame.quit()
