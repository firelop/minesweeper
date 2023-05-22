import pygame, spritesheet, random
from consts import bomb_amount, grid_size, cell_size, TOP_SIZE, BLUE, GREEN, GRAY

def get_grid(default):
    return [[default for x in range(grid_size.get())] for y in range(grid_size.get())]

def proximity_values(bomb_list, bombs_pos):
    pass
    # for bx, by in bombs_pos:
    #     for y in range(3):
    #         for x in range(3):
    #             tx = (bx - x) + 1
    #             ty = (by - y) + 1

    #             if ty < 0 or tx < 0:
    #                 continue

    #             if ty > grid_size.get()-1 or tx > grid_size.get()-1:
    #                 continue

    #             if bomb_list[ty][tx] == -1:
    #                 continue

                
    #             bomb_list[ty][tx] += 1

    # return bomb_list
    

def bomb_generation(bomb_list, x, y):
    bombs_pos = []
    bomb_count = 0
    bomb_amount.set(grid_size.get()**2 // 8)
    print(bomb_amount.get())
    while bomb_count < bomb_amount.get():
        bx = random.randint(0, grid_size.get() - 1)
        by = random.randint(0, grid_size.get() - 1)
        if bx > x+1 or bx < x-1 and by > y+1 or by < y-1:
            bombs_pos.append((bx, by))
            bomb_list[by][bx] = -1
            bomb_count += 1
    
    return proximity_values(bomb_list, bombs_pos)

class Game:
    def __init__(self, window, difficulty):
        print(difficulty)
        self.window = window
        self.difficulty = difficulty
        grid_size.set(difficulty["grid_size"])
        cell_size.set(difficulty["cell_size"])
        bomb_amount.set(difficulty["grid_size"]//8)
        self.resize()
        self.bomb_list = get_grid(0)
        self.first = True
        self.grid = get_grid(-1)
        self.animation_frame = 0
        self.playing = True
        self.animation_frame = 0
        self.sheet = spritesheet.Spritesheet("sprites/flag.png")

    def resize(self):
        self.window = pygame.display.set_mode((cell_size.get()*grid_size.get(), cell_size.get()*grid_size.get() + TOP_SIZE))

    def render(self):
        y = 0
        for _ in range(len(self.grid)):

            for x in range(len(self.grid[y])):
                cell_value = self.grid[y][x]
                if cell_value == 1:
                    self.window.fill(GRAY, (x * cell_size.get(), y * cell_size.get() + TOP_SIZE, cell_size.get(), cell_size.get() + TOP_SIZE))
                    pol = pygame.font.Font("fonts/Orbitron.ttf", 46)
                    if(self.bomb_list[y][x] != 0):
                        txt = pol.render(str(self.bomb_list[y][x]), True, (0, 0, 0))
                        self.window.blit(pygame.transform.scale(txt, (cell_size.get(), cell_size.get())), (x * cell_size.get(), y * cell_size.get() + TOP_SIZE, cell_size.get(), cell_size.get() + TOP_SIZE))

                elif cell_value == 2:
                    self.window.fill(BLUE if (x + y) % 2 == 0 else GREEN,
                                (x * cell_size.get(), y * cell_size.get() + TOP_SIZE, cell_size.get(), cell_size.get() + TOP_SIZE))
                    self.window.blit(
                        pygame.transform.scale(
                            self.sheet.image_at((
                                int(self.animation_frame) * 16, 0, 16, 16
                            )),
                            (cell_size.get(), cell_size.get())
                        ), (x * cell_size.get(), y * cell_size.get() + TOP_SIZE)
                    )
                else:
                    self.window.fill(BLUE if (x + y) % 2 == 0 else GREEN,
                                (x * cell_size.get(), y * cell_size.get() + TOP_SIZE, cell_size.get(), cell_size.get() + TOP_SIZE))

                

            y += 1

            self.animation_frame = (self.animation_frame + 0.016) % 4

    def propagate(self, x, y):
        if(self.bomb_list[y][x] != 0):
            return
        for i in range(3):
            for n in range(3):
                a = (x - n)+1
                b = (y - i)+1
                if a < 0 or b < 0:
                    continue

                if a > grid_size.get()-1 or b > grid_size.get()-1:
                    continue

                if self.bomb_list[b][a] == 0:
                    if self.grid[b][a] == -1:
                        self.grid[b][a] = 1
                        self.propagate(a, b)
                elif self.bomb_list[b][a] != -1:
                    self.grid[b][a] = 1
                    
                


    def click(self, x, y, event):
        y -= TOP_SIZE
        
        if y < 0:
            return
            

        cell_value = self.grid[y // cell_size.get()][x // cell_size.get()]

        

        if event.button == 1:
            if cell_value == -1:
                if(self.first):
                    self.first = False
                    self.bomb_list = bomb_generation(self.bomb_list, x//cell_size.get(), y//cell_size.get())
                self.grid[y // cell_size.get()][x // cell_size.get()] = 1
                self.propagate(x//cell_size.get(), y//cell_size.get())
        elif event.button == 3:
            if cell_value == -1:
                self.grid[y // cell_size.get()][x // cell_size.get()] = 2
            elif cell_value == 2:
                self.grid[y // cell_size.get()][x // cell_size.get()] = -1

    
