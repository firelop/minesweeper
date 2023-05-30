import pygame, spritesheet, random
from consts import bomb_amount, grid_size, cell_size, TOP_SIZE, DARK_GREEN, BLUE, GREEN, BEIGE, DARK_BEIGE, BC_LIST, DARK_GRAY, RED, GOLD

def get_grid(default):
    return [[default for x in range(grid_size.get())] for y in range(grid_size.get())]

def proximity_values(bomb_list, bombs_pos):
    print(len(bombs_pos*9))
    v = 0
    for bx, by in bombs_pos:
        for relative_y in range(by-1, by+2):
            for relative_x in range(bx-1, bx+2):
                v+=1
                if relative_y < 0 or relative_x < 0:
                    continue

                if relative_x > grid_size.get()-1 or relative_y > grid_size.get()-1:
                    continue
                
                if bomb_list[relative_y][relative_x] == -1:
                    continue
                bomb_list[relative_y][relative_x] += 1

    print(v)
    


    return bomb_list, bombs_pos
    

def bomb_generation(bomb_list, x, y):
    bombs_pos = []
    bomb_count = 0
    bomb_amount.set((grid_size.get()**2 // 63)*10)
    print(bomb_amount.get())
    while bomb_count < bomb_amount.get():
        bx = random.randint(0, grid_size.get() - 1)
        by = random.randint(0, grid_size.get() - 1)
        if bomb_list[by][bx] == -1:
            continue
        if bx > x+1 or bx < x-1 and by > y+1 or by < y-1:
            bombs_pos.append((bx, by))
            bomb_list[by][bx] = -1
            bomb_count += 1
    
    return proximity_values(bomb_list, bombs_pos)

class Game:
    def __init__(self, window, difficulty, chrono):
        print(difficulty)
        self.window = window
        self.difficulty = difficulty
        self.chrono = chrono
        grid_size.set(difficulty["grid_size"])
        cell_size.set(difficulty["cell_size"])
        bomb_amount.set(difficulty["grid_size"]//8)
        self.resize()
        self.bomb_list = get_grid(0)
        self.first = True
        self.grid = get_grid(-1)
        self.animation_frame = 0
        self.playing = True
        self.game_over = False
        self.won = False
        self.restart_rect = None
        self.restart = False
        self.bomb_pos = []
        self.flag_pos = []
        self.animation_frame = 0
        self.font = pygame.font.SysFont('fonts/Cabin.ttf', 48)
        self.sheet = spritesheet.Spritesheet("sprites/flag.png")

    def resize(self):
        self.window = pygame.display.set_mode((cell_size.get()*grid_size.get(), cell_size.get()*grid_size.get() + TOP_SIZE))

    def check_flag_win(self):
        checks = [a in self.flag_pos for a in self.bomb_pos]
        return all(checks)

    def flag(self, x, y, event):
        y -= TOP_SIZE
     
        if y < 0:
            return
            
        cell_value = self.grid[y // cell_size.get()][x // cell_size.get()]
        if cell_value == -1 and len(self.flag_pos) < len(self.bomb_pos):
                self.grid[y // cell_size.get()][x // cell_size.get()] = 2
                self.flag_pos.append((x // cell_size.get(), y // cell_size.get()))
                if self.check_flag_win():
                    self.won = True
                    return
        elif cell_value == 2:
                self.grid[y // cell_size.get()][x // cell_size.get()] = -1
                self.flag_pos.remove((x // cell_size.get(), y // cell_size.get()))

    def render(self):
        y = 0
        for _ in range(len(self.grid)):

            for x in range(len(self.grid[y])):
                cell_value = self.grid[y][x]
                if cell_value == 1:
                    self.window.fill(BEIGE if (x + y) % 2 == 0 else DARK_BEIGE,
                                (x * cell_size.get(), y * cell_size.get() + TOP_SIZE, cell_size.get(), cell_size.get() + TOP_SIZE))
                    pol = pygame.font.Font("fonts/SpaceMono-Regular.ttf", 46)
                    if(self.bomb_list[y][x] != 0):
                        txt = pol.render(str(self.bomb_list[y][x]), True, (0, 0, 0))
                        self.window.blit(pygame.transform.scale(txt, (cell_size.get(), cell_size.get())), (x * cell_size.get(), y * cell_size.get() + TOP_SIZE, cell_size.get(), cell_size.get() + TOP_SIZE))
                    
                elif cell_value == 2:
                    self.window.fill(GREEN if (x + y) % 2 == 0 else DARK_GREEN,
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
                    self.window.fill(GREEN if (x + y) % 2 == 0 else DARK_GREEN,
                                (x * cell_size.get(), y * cell_size.get() + TOP_SIZE, cell_size.get(), cell_size.get() + TOP_SIZE))

            y += 1

            self.animation_frame = (self.animation_frame + 0.016) % 4

    def propagate(self, x, y):
        if self.bomb_list[y][x] == -1:
            self.game_over = True
            return

        if self.bomb_list[y][x] != 0:
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
                    self.chrono.restart()
                    self.first = False
                    self.bomb_list, self.bomb_pos = bomb_generation(self.bomb_list, x//cell_size.get(), y//cell_size.get())
                self.grid[y // cell_size.get()][x // cell_size.get()] = 1
                self.propagate(x//cell_size.get(), y//cell_size.get())
    
    def display_game_over(self):

        width = 350
        height = 150
        rect_dimension = pygame.Rect(
            (cell_size.get() * grid_size.get() - width) // 2,
            (cell_size.get()*grid_size.get() +
             TOP_SIZE - height) // 2,
            width, height)

        pygame.draw.rect(self.window, DARK_GRAY, rect_dimension.inflate(10, 10))
        pygame.draw.rect(self.window, BC_LIST, rect_dimension)

        game_over_text = self.font.render("Game Over", True, RED)
        self.window.blit(game_over_text, (
            (cell_size.get() * grid_size.get()) // 2 - game_over_text.get_width() // 2,
            (cell_size.get()*grid_size.get() + TOP_SIZE) // 2 - game_over_text.get_height() // 2 - 40))

        restart_text = self.font.render("Recommencer", True, BLUE)
        self.restart_rect = restart_text.get_rect(center=(
            (cell_size.get() * grid_size.get()) // 2,
            (cell_size.get() * grid_size.get() + TOP_SIZE) // 2 + 20))
        pygame.draw.rect(self.window, BLUE, self.restart_rect.inflate(15, 10), 4)
        self.window.blit(restart_text, self.restart_rect)

    def display_win(self):

        width = 350
        height = 150

        rect_dimension = pygame.Rect(
            (cell_size.get() * grid_size.get() - width) // 2,
            (cell_size.get()*grid_size.get() +
             TOP_SIZE - height) // 2,
            width, height)

        pygame.draw.rect(self.window, DARK_GRAY,
                         rect_dimension.inflate(10, 10))
        pygame.draw.rect(self.window, BC_LIST, rect_dimension)

        game_over_text = self.font.render("You WIN", True, GOLD)
        self.window.blit(game_over_text, (
            (cell_size.get() * grid_size.get()) // 2 -
            game_over_text.get_width() // 2,
            (cell_size.get()*grid_size.get() + TOP_SIZE) // 2 - game_over_text.get_height() // 2 - 40))

        restart_text = self.font.render("Recommencer", True, BLUE)
        self.restart_rect = restart_text.get_rect(center=(
            (cell_size.get() * grid_size.get()) // 2,
            (cell_size.get() * grid_size.get() + TOP_SIZE) // 2 + 20))
        pygame.draw.rect(self.window, BLUE, self.restart_rect.inflate(15, 10), 4)
        self.window.blit(restart_text, self.restart_rect)

    def endGame_clicked(self, pos):
        if self.restart_rect == None:
            return
        if self.restart_rect.collidepoint(pos):
            self.restart = True
