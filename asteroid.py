import pygame;
import random;
from circleshape import CircleShape;
from logger import log_event;
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS;

class Asteroid(CircleShape):
    def __int__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self): # asteroid split logic 
        pygame.sprite.Sprite.kill(self)
        if self.radius <= ASTEROID_MIN_RADIUS: # returns if asteroid is small
            return
        
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS # new asteroid size


        # two asteroids objects are from the originals POS
        new_asteroid1 = Asteroid(self.position, self.position, new_radius)
        new_asteroid2 = Asteroid(self.position, self.position, new_radius)

        # This determines the speed
        new_asteroid1.velocity = pygame.Vector2(0, 1).rotate(angle) * 150
        new_asteroid2.velocity = pygame.Vector2(0, 1).rotate(-angle) * 150