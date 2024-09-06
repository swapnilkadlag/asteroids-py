import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "grey", self.position, self.radius)
        
    def update(self, delta):
        forward = pygame.Vector2(0, 1)
        self.position += self.velocity * delta
