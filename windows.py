import pygame

pygame.init()

def load_menu():
  menu = pygame.display.set_mode((400, 550))
  pygame.display.set_caption("Démineur")

  img_bc = pygame.image.load("img/background.png").convert()

  clock = pygame.time.Clock()
  running = True
  x_bc = 1
  direction = 1
  last_tick = pygame.time.get_ticks()
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          running = False
    
    menu.blit(img_bc, (x_bc, 0))

    current_tick = pygame.time.get_ticks()
    elapsed_time = current_tick - last_tick

    if elapsed_time >= 4:
      x_bc += direction

      if x_bc <= -360:
        direction = 1
      elif x_bc >= 0:
        direction = -1

    last_tick = current_tick

    pygame.display.flip()
    clock.tick(60)

  pygame.quit()

load_menu()