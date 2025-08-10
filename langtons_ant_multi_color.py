import pygame
from pygame.locals import *
import enum
from enum import Enum
from enum import auto
import random
from random import randrange
from random import choice
import sys

ant_amount = sys.argv[1]
grid_size = sys.argv[2]

class Color(Enum):
    WHITE = auto()
    BLACK = auto()
    GREEN = auto()
    BLUE = auto()
    YELLOW = auto()

class Direction(Enum):
    LEFT = auto()
    RIGHT = auto()
    UP = auto()
    DOWN = auto()

class Grid_Tile:
    def __init(self):
        self.position = None
        self.color = None

class Ant:
    def __init__(self, current_position,current_direction,start_color):
        self.current_position = current_position
        self.current_direction = current_direction
        self.start_color = start_color

    def move(self, grid):
        current_tile = grid[int(self.current_position.x)][int(self.current_position.y)]
         #turn 90° clockwise and turn field your color
        if current_tile.color == Color.WHITE:
            match self.current_direction:
                case Direction.UP:
                    self.current_direction = Direction.RIGHT
                    current_tile.color = self.start_color
                    self.current_position.x += 1
                case Direction.DOWN:
                    self.current_direction = Direction.LEFT
                    current_tile.color = self.start_color
                    self.current_position.x -=1
                case Direction.LEFT:
                    self.current_direction = Direction.UP
                    current_tile.color = self.start_color
                    self.current_position.y -=1
                case Direction.RIGHT:
                    self.current_direction = Direction.DOWN
                    current_tile.color = self.start_color
                    self.current_position.y += 1
        #no turn and turn field your color
        elif current_tile.color != Color.WHITE and current_tile.color != self.start_color:
            match self.current_direction:
                case Direction.UP:
                    current_tile.color = self.start_color
                    self.current_position.y += 1
                case Direction.DOWN:
                    current_tile.color = self.start_color
                    self.current_position.y -=1
                case Direction.LEFT:
                    current_tile.color = self.start_color
                    self.current_position.x -=1
                case Direction.RIGHT:
                    current_tile.color = self.start_color
                    self.current_position.x += 1
        #turn 90° counter clockwise and turn field white
        elif current_tile.color == self.start_color:
            match self.current_direction:
                case Direction.UP:
                    self.current_direction = Direction.LEFT
                    current_tile.color = Color.WHITE
                    self.current_position.x -= 1
                case Direction.DOWN:
                    self.current_direction = Direction.RIGHT
                    current_tile.color = Color.WHITE
                    self.current_position.x +=1
                case Direction.LEFT:
                    self.current_direction = Direction.DOWN
                    current_tile.color = Color.WHITE
                    self.current_position.y +=1
                case Direction.RIGHT:
                    self.current_direction = Direction.UP
                    current_tile.color = Color.WHITE
                    self.current_position.y -= 1
        self.current_position.x %= len(grid)
        self.current_position.y %= len (grid[0])

class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 1500, 1200

        self.grid_size = int(grid_size)
        self.grid = None
        self.ants = None
        self.ant_amount = int(ant_amount)
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self.create_grid()
        self.create_ants()
        for ant in self.ants:
            print("x:" + str(ant.current_position.x) + ", y:" + str(ant.current_position.y) + ", " + str(ant.current_direction) + ", " + str(ant.start_color))
        for ant in self.ants:
            self.grid[int(ant.current_position.x)][int(ant.current_position.y)].color = ant.start_color
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
    def on_loop(self):
        # pygame.time.wait(500)
        for ant in self.ants:
            ant.move(self.grid)
            
    def on_render(self):
        self._display_surf.fill("black")
        for x in range(len(self.grid)):
            for y in range(len(self.grid[x])):
                if self.grid[x][y].color == Color.WHITE:
                    pygame.draw.rect(self._display_surf,"grey",pygame.Rect(self.grid[x][y].position.x - self.grid_size / 2, self.grid[x][y].position.y - self.grid_size / 2, self.grid_size, self.grid_size))
                if self.grid[x][y].color == Color.BLACK:
                    pygame.draw.rect(self._display_surf,"black",pygame.Rect(self.grid[x][y].position.x - self.grid_size / 2, self.grid[x][y].position.y - self.grid_size / 2, self.grid_size, self.grid_size))
                if self.grid[x][y].color == Color.GREEN:
                    pygame.draw.rect(self._display_surf,"green",pygame.Rect(self.grid[x][y].position.x - self.grid_size / 2, self.grid[x][y].position.y - self.grid_size / 2, self.grid_size, self.grid_size))
                if self.grid[x][y].color == Color.BLUE:
                    pygame.draw.rect(self._display_surf,"blue",pygame.Rect(self.grid[x][y].position.x - self.grid_size / 2, self.grid[x][y].position.y - self.grid_size / 2, self.grid_size, self.grid_size))
                if self.grid[x][y].color == Color.YELLOW:
                    pygame.draw.rect(self._display_surf,"yellow",pygame.Rect(self.grid[x][y].position.x - self.grid_size / 2, self.grid[x][y].position.y - self.grid_size / 2, self.grid_size, self.grid_size))
        line_y_value = self.grid_size
        while line_y_value < self._display_surf.get_height():
            pygame.draw.line(self._display_surf,"white", pygame.Vector2(0, line_y_value),pygame.Vector2(self._display_surf.get_width(),line_y_value),1)
            line_y_value += self.grid_size
        line_x_value = self.grid_size
        while line_x_value < self._display_surf.get_width():
            pygame.draw.line(self._display_surf,"white", pygame.Vector2(line_x_value, 0),pygame.Vector2(line_x_value,self._display_surf.get_height()),1)
            line_x_value += self.grid_size

        
        for ant in self.ants:
            pygame.draw.circle(self._display_surf,"red",self.grid[int(ant.current_position.x)][int(ant.current_position.y)].position,self.grid_size / 3)
        
       
        pygame.display.flip()
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
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

    def create_ants(self):
        color_choices = [c for c in Color if c != Color.WHITE]
        self.ants = [Ant(pygame.Vector2(random.randrange(0,len(self.grid)), random.randrange(0,len(self.grid[0]))),random.choice(list(Direction)),random.choice(color_choices)) for x in range(self.ant_amount) ]


if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()