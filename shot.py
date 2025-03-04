from circleshape import *
from constants import SHOT_RADIUS

class Shot(Circleshape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
     
    def update(self, dt):
        self.position += self.velocity * dt



