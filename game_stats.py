"""
game_stats

Used to store the GameStats class.
"""
#from pathlib import Path
import json
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class GameStats():
    """Used to store information about the games statistics."""

    def __init__(self, game):
        self.game = game
        self.settings = game.settings
        self.max_score = 0
        self.init_saved_scores()
        self.reset_stats()

    def init_saved_scores(self):
        """Used to initialize the player's saved scores."""
        self.path = self.settings.scores_file
        if self.path.exists() and self.path.stat.__sizeof__() > 80:
            contents = self.path.read_text()
            scores = json.loads(contents)
            self.hi_score = scores.get('hi_score', 0)
        else:
            self.hi_score = 0
            self.save_scores()

    def save_scores(self):
        """Saves player scores to a json file."""
        scores = {
            'hi_score': self.hi_score
        }
        contents = json.dumps(scores, indent='4')
        try:
            self.path.write_text(contents)
        except FileNotFoundError as e:
            print(f'File Not Found: {e.value}')

    def reset_stats(self):
        """Used to reset the player's stats."""
        self.ships_left = self.settings.starting_ship_count
        self.score = 0
        self.level = 1

    def update(self, collisions):
        """Used to update the users score and the max score."""
        self._update_score(collisions)

        self._update_max_score()

        self._update_hi_score()

    def _update_max_score(self):
        """Used to update the user's max score."""
        if self.score > self.max_score:
            self.max_score = self.score
        #print(f'Max: {self.max_score}')

    def _update_hi_score(self):
            """Used to update the user's hi score."""
            if self.score > self.hi_score:
                self.hi_score = self.score

    def _update_score(self, collisions):
        """Used to update the aliens users score."""
        for alien in collisions.values():
            self.score += self.settings.alien_points
        #print(f'Basic: {self.score}')

    def update_level(self):
        """Used to update the game's level."""
        self.level += 1
        #print(self.level)