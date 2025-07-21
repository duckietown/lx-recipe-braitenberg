"""Random Duckie placement script."""

import random

from packages.duckiematrix_engine.entities.matrix_entity import (
    MatrixEntityBehavior,
)


class RandomDuckiePlacementScript(MatrixEntityBehavior):
    """Random Duckie placement script."""

    _random_x: float
    _random_y: float

    def __init__(
        self,
        matrix_key: str,
        world_key: str | None,
        x_min: float = -0.5,
        x_max: float = 4.5,
        y_min: float = -0.5,
        y_max: float = 4.5,
    ) -> None:
        """Initialize random Duckie placement script."""
        super().__init__(matrix_key, world_key)
        self._random_x = random.uniform(x_min, x_max)
        self._random_y = random.uniform(y_min, y_max)

    def update(self, _: float) -> None:
        """Update."""
        if self.pose:
            self.pose.x = self._random_x
            self.pose.y = self._random_y
            self.pose.commit()
