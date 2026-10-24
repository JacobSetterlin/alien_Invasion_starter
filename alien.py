"""
alien

Used to hold the alien class.
"""

import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from alien_fleet import AlienFleet

class Alien(Sprite):
    """Used to create bullets for the player to shoot."""

    def __init__(self, fleet: 'AlienFleet', x: float, y: float):
        """Used to create bullets."""
        super().__init__()
        self.fleet = fleet
        self.screen = fleet.game.screen
        self.boundaries = fleet.game.screen.get_rect()
        self.settings = fleet.settings

        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(self.image, 
            (self.settings.bullet_w, self.settings.bullet_h))
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self):
        """Used to update the status of an alien."""
        temp_speed = self.settings.fleet_speed
        
        self.x +=  temp_speed * self.fleet.fleet_direction
        self.rect.x = self.x
        self.rect.y = self.y

    def check_edges(self):
        """Checks if an alien is at the edge of the screen."""
        return (self.rect.right >= self.boundaries.right or self.rect.left <= self.boundaries.left)

    def draw_alien(self):
        """Used to draw aliens onto the window."""
        self.screen.blit(self.image, self.rect)
        