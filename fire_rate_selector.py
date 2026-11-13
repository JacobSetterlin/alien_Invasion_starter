"""
fire rate selector

Used to hold the FireRateSelector class
"""

import random
from fire_rate import FireRate
import pygame
from pathlib import Path
from typing import TYPE_CHECKING
from settings import Settings
import pygame

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class FireRateSelector:
    """Used to manage the player ship's fire rate."""

    def __init__(self, game: 'AlienInvasion'):
        self.game = game
        self.settings = Settings()

    def ask_player(self):
        """Used to ask the player to choose a fire rate."""
        fire_rates = [FireRate(5,1),
                      FireRate(4,2),
                      FireRate(3,3),
                      FireRate(4,2),
                      FireRate(1,5)]

        self.chosen_fire_rates = self._select_fire_rates(fire_rates)

        self._display_fire_rates()

    def _select_fire_rates(self, fire_rates):
        """Selects random fire rates for the player to choose from."""
        chosen_fire_rates = []
        
        rate_one = random.randint(1, len(fire_rates) - 1)
        chosen_fire_rates.append(fire_rates[rate_one])

        rate_two = random.randint(1, len(fire_rates) - 1)
        chosen_fire_rates.append(fire_rates[rate_two])

        return chosen_fire_rates

    def _display_fire_rates(self):
        """Displays the users ability to choose firerates from the screen."""
        while True:
            font = pygame.font.Font(Path.cwd() / 'Assets' / 'Fonts' / 'Silkscreen' / 'Silkscreen-Bold.ttf')
            
            message_one = font.render(f'Option 1: {str(self.chosen_fire_rates[0].amount_of_bullets)}  bullets and {str(self.chosen_fire_rates[0].penetration)} penetration.', True, (255,255,255))
            message_two = font.render(f'Option 2: {str(self.chosen_fire_rates[1].amount_of_bullets)}  bullets and {str(self.chosen_fire_rates[1].penetration)} penetration.', True, (255,255,255))

            self.game.screen.blit(message_one, message_one.get_rect(center=(self.settings.screen_w / 2, self.settings.screen_h / 2)))
            self.game.screen.blit(message_two, message_two.get_rect(center=(self.settings.screen_w / 2, self.settings.screen_h / 2 + 50)))
            pygame.display.flip()

            selected = False

            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_1:
                        print("one")
                        selected = True

                    elif event.key == pygame.K_2:
                        print('two')
                        selected = True

            if selected == True:
                break

        #This was added to fix a bug in which the player lost all control 
        #after selecting a fire rate
        keys = pygame.key.get_pressed()
        self.game.ship.moving_right = keys[pygame.K_RIGHT]
        self.game.ship.moving_left = keys[pygame.K_LEFT]