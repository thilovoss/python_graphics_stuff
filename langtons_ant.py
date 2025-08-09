import pygame
from pygame.locals import *
import enum
from enum import Enum
from enum import auto

class Color(Enum):
    WHITE = auto()
    BLACK = auto()

class Direction(Enum):
    LEFT = auto()
    RIGHT = auto()
    UP = auto()
    DOWN = auto()

class Grid_Tile:
    def __init(self):
        self.position = None
        self.color = None

class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 800, 600
        self.clock = pygame.time.Clock()
        self.grid_size = 10
        self.grid = None
        self.dt = 0
        self.circle_pos = None
        self.circle_dir = None
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self.create_grid()
        self.circle_pos = pygame.Vector2(int(len(self.grid) / 2),int(len(self.grid[0]) / 2))
        self.direction = Direction.UP
        self.grid[int(self.circle_pos.x)][int(self.circle_pos.y)].colored = True
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
    def on_loop(self):
        # pygame.time.wait(1)

        self.dt = self.clock.tick(60) / 1000
    
        # Rules
        current_tile = self.grid[int(self.circle_pos.x)][int(self.circle_pos.y)]
        if current_tile.color == Color.WHITE:
            match self.direction:
                case Direction.UP:
                    self.direction = Direction.RIGHT
                    current_tile.color = Color.BLACK
                    self.circle_pos.x += 1
                case Direction.DOWN:
                    self.direction = Direction.LEFT
                    current_tile.color = Color.BLACK
                    self.circle_pos.x -=1
                case Direction.LEFT:
                    self.direction = Direction.UP
                    current_tile.color = Color.BLACK
                    self.circle_pos.y -=1
                case Direction.RIGHT:
                    self.direction = Direction.DOWN
                    current_tile.color = Color.BLACK
                    self.circle_pos.y += 1
        elif current_tile.color == Color.BLACK:
            match self.direction:
                case Direction.UP:
                    self.direction = Direction.LEFT
                    current_tile.color = Color.WHITE
                    self.circle_pos.x -= 1
                case Direction.DOWN:
                    self.direction = Direction.RIGHT
                    current_tile.color = Color.WHITE
                    self.circle_pos.x +=1
                case Direction.LEFT:
                    self.direction = Direction.DOWN
                    current_tile.color = Color.WHITE
                    self.circle_pos.y +=1
                case Direction.RIGHT:
                    self.direction = Direction.UP
                    current_tile.color = Color.WHITE
                    self.circle_pos.y -= 1
        
        self.circle_pos.x %= len(self.grid)
        self.circle_pos.y %= len (self.grid[0])
            
    def on_render(self):
        self._display_surf.fill("black")
        for x in range(len(self.grid)):
            for y in range(len(self.grid[x])):
                if self.grid[x][y].color == Color.WHITE:
                    pygame.draw.rect(self._display_surf,"grey",pygame.Rect(self.grid[x][y].position.x - self.grid_size / 2, self.grid[x][y].position.y - self.grid_size / 2, self.grid_size, self.grid_size))
                if self.grid[x][y].color == Color.BLACK:
                    pygame.draw.rect(self._display_surf,"black",pygame.Rect(self.grid[x][y].position.x - self.grid_size / 2, self.grid[x][y].position.y - self.grid_size / 2, self.grid_size, self.grid_size))
        line_y_value = self.grid_size
        while line_y_value < self._display_surf.get_height():
            pygame.draw.line(self._display_surf,"white", pygame.Vector2(0, line_y_value),pygame.Vector2(self._display_surf.get_width(),line_y_value),1)
            line_y_value += self.grid_size
        line_x_value = self.grid_size
        while line_x_value < self._display_surf.get_width():
            pygame.draw.line(self._display_surf,"white", pygame.Vector2(line_x_value, 0),pygame.Vector2(line_x_value,self._display_surf.get_height()),1)
            line_x_value += self.grid_size

        

        pygame.draw.circle(self._display_surf,"blue",self.grid[int(self.circle_pos.x)][int(self.circle_pos.y)].position,self.grid_size / 3)
       
        pygame.display.flip()
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_render()
            self.on_loop()
        self.on_cleanup()

    def create_grid(self):
        columns, rows = int(self._display_surf.get_height() / self.grid_size), int(self._display_surf.get_width() / self.grid_size)
        self.grid = [[0 for x in range(columns)] for y in range(rows)]
        x_pos = self.grid_size / 2
        y_pos = self.grid_size / 2
        for x in range(len(self.grid)):
            for y in range(len(self.grid[x])):
                grid_tile = Grid_Tile()
                grid_tile.color = Color.WHITE
                grid_tile.position = pygame.Vector2(x_pos,y_pos)
                self.grid[x][y] = grid_tile
                y_pos += self.grid_size
            y_pos = self.grid_size / 2
            x_pos += self.grid_size
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()