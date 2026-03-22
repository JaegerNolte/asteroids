import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    # groups made to better manage game objects
    updatable = pygame.sprite.Group() 
    drawable = pygame.sprite.Group()

    # player class is added to both groups
    player.add(updatable)
    player.add(drawable)

    # Player is the name of the class, not an instance of it
    # This must be done before any Player objects are created
    Player.containers = (updatable, drawable)


    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    

        screen.fill("black")
        updatable.update(dt) # updates objects in the updatable group
        for object in drawable: # loops drawables and .draw() them indiviudally 
            object.draw(screen)
        pygame.display.flip() # refreshes franes
        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
