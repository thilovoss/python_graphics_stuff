import pygame
from pygame.locals import *

class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 800, 600
        self.clock = pygame.time.Clock()
        self.grid_size = 200
        self.grid = None
        self.dt = 0
        self.circle_pos = None
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self.create_grid()
        self.circle_pos = pygame.Vector2(0,0)
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
    def on_loop(self):
        pygame.time.wait(300)

        self.dt = self.clock.tick(60) / 1000
        if self.circle_pos.x < len(self.grid) -1 :
            self.circle_pos.x += 1
        else:
            self.circle_pos.x = 0
            if self.circle_pos.y < len (self.grid[0])-1:
                self.circle_pos.y += 1
            else: 
                self.circle_pos.y = 0
            
            
    def on_render(self):
        self._display_surf.fill("black")
        line_y_value = self.grid_size
        while line_y_value < self._display_surf.get_height():
            pygame.draw.line(self._display_surf,"white", pygame.Vector2(0, line_y_value),pygame.Vector2(self._display_surf.get_width(),line_y_value),1)
            line_y_value += self.grid_size
        line_x_value = self.grid_size
        while line_x_value < self._display_surf.get_width():
            pygame.draw.line(self._display_surf,"white", pygame.Vector2(line_x_value, 0),pygame.Vector2(line_x_value,self._display_surf.get_height()),1)
            line_x_value += self.grid_size

        pygame.draw.circle(self._display_surf,"red",self.grid[int(self.circle_pos.x)][int(self.circle_pos.y)],self.grid_size / 3)
       
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
                self.grid[x][y] = pygame.Vector2(x_pos,y_pos)
                y_pos += self.grid_size
            y_pos = self.grid_size / 2
            x_pos += self.grid_size
        for row in self.grid:
            print(" ".join(f"({v.x}, {v.y})" for v in row))
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()