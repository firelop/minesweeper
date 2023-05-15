import pygame

pygame.init()

class SelectList:
  def __init__(self, options, position, size):
    self.options = options  
    self.position = position
    self.size = size
    self.open = False
    self.selected_option = None
    self.police = pygame.font.Font("./fonts/Orbitron.ttf", int(size[1]/2))

  def display(self, window):
    bc_color = (210, 210, 210)
    txt_color = (50, 50, 50)
    width = self.size[0]
    height = self.size[1]
    x = self.position[0]
    y = self.position[1]

    pygame.draw.rect(window, bc_color, (x, y - height // 2, width, height))

    txt = "Difficultée"
    txt_area = self.police.render(txt, True, txt_color)
    window.blit(txt_area, (x + width // 2 - txt_area.get_width() // 2, y - txt_area.get_height() // 2))

  def display_subOption(self):
    pass

  def mouse_clic(self, mouse_position):
    if mouse_position[0] >= self.position[0] and mouse_position[0] <= self.position[0] + self.size[0]:
        if mouse_position[1] >= self.position[1] // 2 and mouse_position[1] <= self.position[1] + self.size[1] // 2:
            self.open = not self.open
            print(self.open)
