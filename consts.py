GRID_SIZE = 7
CELL_SIZE = 50
BOMB_AMOUNT = int((GRID_SIZE ** 2) / 8)

TOP_SIZE = 75
BLUE = (132, 196, 209)
GREEN = (50, 144, 143)
GRAY = (232, 246, 238)
RED = (200, 25, 25)
DARK_GRAY = (128, 128, 128)

DIFFICULTIES = {
    "easy": {"grid_size": 10, "cell_size": 50},
    "medium": {"grid_size": 15, "cell_size": 35},
    "hard": {"grid_size": 20, "cell_size": 30}
}

class ChangingValues:
    def __init__(self, value):
        self.value = value
    
    def set(self, value):
        self.value = value
    
    def get(self):
        return self.value
    
difficulty = ChangingValues("easy")

grid_size = ChangingValues(10)
cell_size = ChangingValues(50)
bomb_amount = ChangingValues(int((grid_size.get() ** 2) / 8))


