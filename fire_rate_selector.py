"""
fire rate selector

Used to hold the FireRateSelector class
"""

import random
from fire_rate import FireRate

class FireRateSelector:
    """Used to manage the player ship's fire rate."""

    def __init__(self):
        pass

    def ask_player(self):
        fire_rates = [FireRate(5,1),
                      FireRate(4,2),
                      FireRate(3,3),
                      FireRate(4,2),
                      FireRate(1,5)]

        chosen_fire_rates = self._select_fire_rates(fire_rates)

    def _select_fire_rates(self, fire_rates):
        chosen_fire_rates = []
        
        rate_one = random.randint(1, len(fire_rates) - 1)
        chosen_fire_rates.append(rate_one)

        rate_two = random.randint(1, len(fire_rates) - 1)
        chosen_fire_rates.append(rate_two)

        return chosen_fire_rates