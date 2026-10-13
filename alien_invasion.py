"""
Alien Invasion
Jacob Setterlin

Holds the main logic of Alien Invasion.
"""

import sys
import pygame

class AlienInvasion:
    """Used to control the pygame window."""

    def __init__(self):
        """Used to create the window of Alien Invasion"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")
        
        self.running = True

    def run_game(self):
        """Used to close a pygame window when the user hits the x on the window"""
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()