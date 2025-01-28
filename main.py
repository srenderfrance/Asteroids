import pygame
from player import *
from pygame.locals import *
pygame.init()
from constants import *
from asteroidfield import *

clock = pygame.time.Clock() 
dt = 0
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
all_shots = pygame.sprite.Group()
Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable)
Shot.containers = (updatable, drawable, all_shots)

def main():
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    asteroidfield = AsteroidField()

    while True:
        screen.fill('black')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        tt = clock.tick(60)
        dt = tt/1000
        for thing in updatable:
            thing.update(dt)
        for thing in asteroids:
            if player.collision_check(thing):
                print("Game over!")
                pygame.QUIT
                return
        for shot in all_shots:
            for thing in asteroids:
                if shot.collision_check(thing):
                    shot.kill()
                    thing.split()


if __name__ == "__main__":
    main()
