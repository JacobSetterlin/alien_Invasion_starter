"""
fire rate

Used to hold the fire_rate class.
"""

class FireRate:
    """Used to create objects for the ships fire rate."""

    def __init__(self, amount_of_bullets: int, penetration: int):
        """Used to create fire rates."""
        self.amount_of_bullets = amount_of_bullets
        self.penetration = penetration