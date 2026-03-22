import pygame;
from circleshape import CircleShape;
from constants import LINE_WIDTH, PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED;


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, dt): # rotate logic
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1) # starts with a unit vector facing down
        rotated_vector = unit_vector.rotate(self.rotation) # rotate the vector, so its facing the same direction as the player
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt # multiply the vector by player_speed * 2, so the vector is the length the player should move this frame
        self.position += rotated_with_speed_vector # add the vector to the players POS

    def update(self, dt): # inputs for rotating
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.move(dt)
        
        if keys[pygame.K_s]:
            self.rotate(dt * -1)

        if keys[pygame.K_a]:
            self.rotate(dt * -1)
            
        if keys[pygame.K_d]:
            self.rotate(dt)


    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]