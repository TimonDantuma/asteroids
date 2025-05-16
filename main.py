import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *
from circleshape import *
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    pygame_clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    
    
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    

    new_player = Player(x, y, shots)
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for entity in drawable:
            entity.draw(screen)
        updatable.update(dt)
        collisions_detected = 0
        for asteroid in asteroids:
            if CircleShape.collision_check(new_player, asteroid):
                print("Game over!")
                raise SystemExit()
        for asteroid in asteroids:
            for shot in shots:
                if CircleShape.collision_check(shot, asteroid):
                    shot.kill()
                    asteroid.split()
                    collisions_detected += 1 
        pygame.display.flip()
        dt = pygame_clock.tick(60) / 1000

    #print("Starting Asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
