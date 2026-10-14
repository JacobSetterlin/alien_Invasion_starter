"""
ship
Jacob Setterlin

This file is used to hold the Ship class.
"""

import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Ship:
    """Used to manage how the player's ship displayes to the pygame window."""

    def __init__(self, game: "AlienInvasion"):
        """
            Used to manage the settings of the ship.
        """
        
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(self.image, 
            (self.settings.ship_w, self.settings.ship_h))

        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def draw(self):
        """Used to draw the ship onto the pygame window."""
    
        self.screen.blit(self.image, self.rect)