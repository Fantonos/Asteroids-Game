from constants import *
from circleshape import CircleShape
from shot import Shot
import pygame

'''
Create a new file called player.py with a Player class that inherits from CircleShape.

The Player constructor should take x and y integers as input, then:

Call the parent class's constructor, also passing in PLAYER_RADIUS
Create a field called rotation, initialized to 0
Paste this triangle method into your Player class:


'''
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.PLAYER_SHOOT_COOLDOWN = 0 
    
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
        
    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.rotation += PLAYER_TURN_SPEED * dt
        if keys[pygame.K_a]:
            self.rotation -= PLAYER_TURN_SPEED * dt
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.position -= pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SPEED * dt
        if keys[pygame.K_SPACE]:
            self.shoot()
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt  
    
    def shoot(self):
        if self.PLAYER_SHOOT_COOLDOWN > 0:
            return
        self.PLAYER_SHOOT_COOLDOWN = PLAYER_SHOOT_COOLDOWN  
        shot = Shot(self.position, self.rotation, SHOT_RADIUS)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        
        
        
    