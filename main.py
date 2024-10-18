import pygame
from constants import *

def main():
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_loop(screen)
    print("Starting asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}') 
    print(f'Screen height: {SCREEN_HEIGHT}')


def game_loop(screen):
    while True:
        screen.fill("black")
        pygame.display.update()
        # This will check if the user has closed the window and exit the game loop if they do. It will make the window's close button work.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        




if __name__ == "__main__":
    main()
    



