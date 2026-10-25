"""
alien_invasion

Holds the main logic of the game.
"""

import sys
import pygame
from settings import Settings
from ship import Ship
from arsenal import Arsenal
#from alien import Alien
from alien_fleet import AlienFleet
from game_stats import GameStats
from time import sleep

class AlienInvasion:
    """Used to control the pygame window."""

    def __init__(self):
        """Used to create the window of Alien Invasion"""
        pygame.init()
        self.settings = Settings()
        self.gamestats = GameStats(self.settings.starting_ship_count)

        self.screen = pygame.display.set_mode(
            (self.settings.screen_w, self.settings.screen_h)
            )
        pygame.display.set_caption(self.settings.name)
        
        self.running = True
        self.clock = pygame.time.Clock()

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg, 
            (self.settings.screen_w, self.settings.screen_h))

        self.ship = Ship(self, Arsenal(self))
        self.alien_fleet = AlienFleet(self)
        self.alien_fleet.create_fleet()

        self.game_active = True
        
        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)
        self.laser_sound.set_volume(0.3)
        
        self.impact_sound = pygame.mixer.Sound(self.settings.impact_sound)
        self.impact_sound.set_volume(0.3)

    def run_game(self):
        """Used to manage the pygame window."""
        while self.running:
            self._check_events()
            if self.game_active:
                self.ship.update()
                self.alien_fleet.update_fleet()
                self._check_collisions()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _check_collisions(self):
        """Used to check if aliens or the ship are colliding with anything."""
        if self.ship.check_collisions(self.alien_fleet.fleet):
            self._check_game_status()
        
        if self.alien_fleet.check_fleet_bottom():
            self._check_game_status()
        
        collisions = self.alien_fleet.check_collisions(self.ship.arsenal.arsenal)
        if collisions:
            self.impact_sound.play()
            self.impact_sound.fadeout(500)

        if self.alien_fleet.check_destroyed_status():
             self._reset_level()

    def _check_game_status(self):
        """Used the check information about the state of the game."""
        if self.gamestats.ships_left > 0:
            self.gamestats.ships_left -= 1
            self._reset_level()
            sleep(0.5)
        else:
            self.game_active = False

         
    def _reset_level(self):
        """Used to reset the level."""
        self.ship.arsenal.arsenal
        self.alien_fleet.fleet.empty()
        self.alien_fleet.create_fleet()
    
    def _update_screen(self):
        """Used to display sprites"""
        self.screen.blit(self.bg, (0,0))
        self.ship.draw()
        self.alien_fleet.draw()
        pygame.display.flip()

    def _check_events(self):
        """Used to check for events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        """Checks if the player is pressing any buttons."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            if self.ship.fire():
                self.laser_sound.play()
                self.laser_sound.fadeout(250)

    def _check_keyup_events(self, event):
        """Checks if the player is releasing a button."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_q:
            self.running = False
            pygame.quit()
            sys.exit()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()