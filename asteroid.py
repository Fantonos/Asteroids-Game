from circleshape import CircleShape
import pygame
import random
from constants import *



class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)
        self.rotation = 0
        self.rotation_speed = 0

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        for i in [-1, 1]:
            rand__blue_angle = random.uniform(20, 50)
            Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS).velocity = pygame.Vector2(0, 1.2).rotate(rand__blue_angle * i) * 100
        
        