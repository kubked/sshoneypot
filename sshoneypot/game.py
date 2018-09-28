"""Module with all game related classes"""


class Bird:
    """Bird class representing player.

    Provides all needed tools for updating and drawing itself.

    .. note::

        Bird check collisions with objects present on canvas.
        It's important to keep drawing order!
        Draw objects which should collide with bird first.
    """
    def __init__(self):
        self.y = 50
        self.velocity = 0
        self.acceleration = -9.81

    def next_frame(self, time=1/60):
        """Update bird position, rotation and vertical velocity."""
        pass

    def draw(self, canvas):
        """Draw bird in its current position.

        Args:
            canvas (drawille.Canvas): Canvas with current game board.
                Bird should be drew on that canvas.
        :rtype: bool indicating whether bird is not colliding with anything
        """
        return False

    def _draw_pixel(self, canvas, x, y):
        """Draw pixel of bird and check collisions with objects"""
        filled = canvas.get(x, y)
        canvas.set(x, y)
        return not filled
