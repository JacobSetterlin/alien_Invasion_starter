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
        self.boundaries = self.screen.get_rect()

        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(self.image, 
            (self.settings.ship_w, self.settings.ship_h))

        self.rect = self.image.get_rect()
        self.rect.midbottom = self.boundaries.midbottom

        self.moving_right = False
        self.moving_left = False
        self.x = float(self.rect.x)

    def update(self):
        """Used to update the ships position when the player presses keys."""
        temp = self.settings.ship_speed
        if self.moving_right and self.rect.right < self.boundaries.right:
            self.x += temp
            
        if self.moving_left and self.rect.left > self.boundaries.left:
            self.x -= temp

        self.rect.x = self.x

    def draw(self):
        """Used to draw the ship onto the pygame window."""
    
        self.screen.blit(self.image, self.rect)