from duckiematrix_engine.template import MatrixEntityBehavior

import random

class RandomDuckiePlacement(MatrixEntityBehavior):

    def __init__(self, *args,
                 x_min: float = -0.5,
                 x_max: float = 4.5,
                 y_min: float = -0.5,
                 y_max: float = 4.5):
        super(RandomDuckiePlacement, self).__init__(*args)
        self.rand_x = random.uniform(x_min, x_max)
        self.rand_y = random.uniform(y_min, y_max)

    def update(self, delta_t: float):
        # not sure why this has to be done in update
        self.pose.x = self.rand_x
        self.pose.y = self.rand_y
        self.pose.commit()
