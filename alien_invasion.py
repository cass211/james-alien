#Alien Invasion program as outlined in Python Crash Course 2nd Edition
import sys

import pygame

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
#pygame init function initializes the background settings that Pygame needs to work
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
    def run_game(self):
#The game is controlled by the run_game method
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            #This is an event loop looking for player to quit the game.

            pygame.display.flip()
#pygame.display.flip updates the display to show the new positions of the game elements and hide the old one.

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
#This is a created instance of run_game in an if block that only runs if the file is called directly.
