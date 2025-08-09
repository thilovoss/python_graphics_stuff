import pygame
from pygame.locals import *
import random
import math
 
class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 640, 400
        self.circle_pos = None
        self.clock = pygame.time.Clock()
        self.direction = pygame.Vector2(1,1)
        self.dt = 0
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.circle_pos = pygame.Vector2(self._display_surf.get_width() / 2, self._display_surf.get_height() / 2)
        self._running = True
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
    def on_loop(self):
        if self.circle_pos.y < 0 or self.circle_pos.y > self._display_surf.get_height():
            self.direction.y = -self.direction.y
        if self.circle_pos.x > self._display_surf.get_width() or self.circle_pos.x < 0:
            self.direction.x = -self.direction.x
        
        self.circle_pos.x += 100 * self.direction.x * self.dt
        self.circle_pos.y += 100 * self.direction.y * self.dt
        
        # print(self.circle_pos.x)
        # print(self.circle_pos.y)
        # print("\n")

        self.dt = self.clock.tick(60) / 1000
    def on_render(self):
        self._display_surf.fill("black")
        pygame.draw.circle(self._display_surf, "red", self.circle_pos, 10)
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
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()

