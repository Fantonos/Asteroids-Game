import pygame
from constants import *
from player import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    game_loop(screen, clock, game_player)
    print("Starting asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}') 
    print(f'Screen height: {SCREEN_HEIGHT}')


def game_loop(screen, clock, player):
    while True:
        for event in pygame.event.get():# This below will check if the user has closed the window and exit the game loop if they do. It will make the window's close button work.
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000 # dt is the time between frames
        player.rotate(dt)
        screen.fill("black")
        player.draw(screen)
        pygame.display.update()

        
        




if __name__ == "__main__":
    main()
    



